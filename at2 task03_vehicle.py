"""Q3: Vehicle registration normalisation and validation using string operations."""

def normalise(text):
    return text.strip().replace(" ", "").replace("-", "").upper()

def is_valid(reg):
    if len(reg) not in (9, 10):
        return False
    if not reg[0:2].isalpha() or not reg[2:4].isdigit():
        return False
    if len(reg) == 9:
        return reg[4:5].isalpha() and reg[5:9].isdigit()
    return reg[4:6].isalpha() and reg[6:10].isdigit()

def format_receipt(reg):
    if not is_valid(reg):
        raise ValueError("Cannot format an invalid registration")
    return f"{reg[0:2]} {reg[2:4]} {reg[4:-4]} {reg[-4:]}"

if __name__ == "__main__":
    samples = ["tn 09 ab 1234", "KA-01-M-0007", "TN9AB1234",
               "TN 22 1234 AB", "mh 12 xy 9876", "12-AB-CD-1234"]
    print("Input              | Normalised | Result")
    for raw in samples:
        reg = normalise(raw)
        print(f"{raw:18} | {reg:11} | {'valid' if is_valid(reg) else 'INVALID'}")
        if is_valid(reg):
            print("  Receipt:", format_receipt(reg))
