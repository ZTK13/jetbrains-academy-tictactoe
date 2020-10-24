def what_to_do(instructions):
    prefix = "I "
    if instructions.startswith("Simon says") or \
            instructions.endswith("Simon says"):
        suffix = instructions.replace("Simon says", "").strip()
    else:
        suffix = "won't do it!"
    return prefix + suffix
