text = "Привет, мир!"
morse_dict = {
    "a" = "· −"
    "б" = "− · · ·"
    "в" = "· − −"
    "г" = "− − ·"
    "д" = "− · ·"
    "е и ё" = "·"
    "ж" = "· · · −"
    "з" = "− − · ·"
    "и" = "· ·"
    "й" = "· − − −"
    "к" = "− · −"
    "л" = "· − · ·"
    "м" = "− −"
    "н" = "− ·"
    "о" = "− − −"
    "п" = "· − − ·"
    "р" = "· − ·"
    "с" = "· · ·"
    "т" = "−"
    "у" = "· · −"
    "ф" = "· · − ·"
    "х" = "· · · ·"
    "ц" = "− · − ·"
    "ч" = "− − − ·"
    "ш" = "− − − −"
    "щ" = "− − · −"
    "ъ и ь" = "− · · −"
    "ы" = "− − · −"
    "э" = "· · − · ·"
    "ю" = "· · − −"
    "я" = "· − · −"

}


def encode_morse(text: str) -> str:
	text = text.lower()
    result_list = []

    for i in text:
    	result_list.append(morse_dict[i])

    return " "result_list

text = "Привет, мир!"
encode_morse(text)
