def apply_style(style, text):
    styles = {
        "Genius": f"Obviously, this is trivial. {text}",
        "Intern": f"Umm… I think this might help? {text}",
        "Professor": f"Let's examine this step by step. {text}",
        "Reviewer": f"Wow, groundbreaking. {text}"
    }
    return styles.get(style, text)

