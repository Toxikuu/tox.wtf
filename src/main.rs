use std::ffi::OsStr;
use std::fs::{self, read_dir};
use fshelpers::mkf_p;
use walkdir::WalkDir;
use std::path::{Path, PathBuf};

use minijinja::{context, Environment};
use color_eyre::Result;

fn render_root(env: &Environment) -> Result<()> {
    let template = env.get_template("index.html")?;
    let rendered = template.render(context! {})?;

    let path = Path::new("target/site/index.html");

    mkf_p(path)?;
    fs::write(path, rendered)?;

    Ok(())
}

fn render_error_pages(env: &Environment) -> Result<()> {
    let mut env = env.clone(); // TODO: Consider whether I mind mangling the base env

    for f in read_dir("pages/e")?.flatten() {
        let path = f.path();
        if path.extension().and_then(|e| e.to_str().map(|s| s == "html")).unwrap_or(false) {
            add_template_from_path(&mut env, &path)?;

            // FIXME: Log failures here
            let Some(filename) = path.file_name().and_then(|f| f.to_str()) else { continue };

            let template = env.get_template(filename)?;
            let rendered = template.render(context! {})?;

            let path = Path::new("target/site/e").join(filename);

            mkf_p(&path)?;
            fs::write(path, rendered)?;
        }
    }

    Ok(())
}

fn should_template<P: AsRef<Path>>(path: P) -> bool {
    let path = path.as_ref();
    path.is_file() &&
        path.extension().and_then(|e| e.to_str().map(|s| s == "html")).unwrap_or(false)
}

// Collect pages recursively
fn collect_pages() -> Vec<PathBuf> {
    WalkDir::new("pages")
        .min_depth(2) // TODO: Should be 1 ideally
        .into_iter()
        .filter_map(|e| e.map(|e| e.path().to_path_buf()).ok())
        .filter(|e| e.is_file())
        .filter(|e| e.iter().any(|p| p.to_string_lossy() != "e"))
        .filter(|e| e.extension() == Some(OsStr::new("html")))
        .collect::<Vec<_>>()
}

fn render_pages(env: &Environment) -> Result<()> {
    let mut env = env.clone();

    for f in collect_pages() {
        add_template_from_path(&mut env, &f)?;
        let Some(filename) = f.file_name().and_then(|f| f.to_str()) else { continue };

        let template = env.get_template(filename)?;
        let rendered = template.render(context! {})?;

        let path = Path::new("target/site/").join(f.to_string_lossy().trim_start_matches("pages/"));

        mkf_p(&path)?;
        fs::write(path, rendered)?;
    }

    Ok(())
}

// TODO: Don't abuse leak
fn add_template_from_path<P>(env: &mut Environment, path: P) -> Result<()>
where P: AsRef<Path>,
{
    let path = path.as_ref();
    let str = fs::read_to_string(path)?.leak();
    let path_str = path.file_name().unwrap().to_str().unwrap().to_string().leak();

    env.add_template(
        path_str,
        str,
    )?;

    Ok(())
}

fn main() -> Result<()> {
    let mut env = Environment::new();

    add_template_from_path(&mut env, "pages/macros.html")?;
    add_template_from_path(&mut env, "pages/base.html")?;
    add_template_from_path(&mut env, "pages/index.html")?;

    render_root(&env)?;
    render_error_pages(&env)?;
    render_pages(&env)?;

    Ok(())
}
