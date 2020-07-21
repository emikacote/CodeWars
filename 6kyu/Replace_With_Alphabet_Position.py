import re
def alphabet_position(text):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    text = text.replace(' ','')
    text = text.lower().strip("123456789")
    text = re.sub(r'[^\w\d\s\b]','', text)  # obviously didn't understand regex very well
    for i, c in enumerate(text):
        num = alpha.rfind(c) + 1
        text = text.replace(c,str(num)+" ")
    return text.strip()
