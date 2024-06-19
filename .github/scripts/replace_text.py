"""Simple CI script to make files ready for deployment via value replacement

Should be run from the main/root directory of the project
"""

from pathlib import Path


def main():
    # Those are public keys to be put in HTML, not secrets
    localhost_recaptcha = "6LeO1vspAAAAABu8s4D8XPFdncUIw5jIy2Fv6Cbj";
    production_recaptcha = "6LdPzPspAAAAAGfQOpCPB0eLoPxjAqaJvajPlJaa";

    contact_file = Path("docs/index.md")
    content = contact_file.read_text(encoding="utf-8")
    result = content.replace(localhost_recaptcha, production_recaptcha)
    contact_file.write_text(result, encoding="utf-8")


if __name__ == "__main__":
    main()
