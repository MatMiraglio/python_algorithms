
def urlify(self, string, length) -> str:

    backSlider = len(string) - 1

    for i in reversed(range(length)):
        if string[i] ==' ':
            string[backSlider - 3 :backSlider] = '%20'
            backSlider -= 3
        else:
            string[backSlider] = string[i]
            backSlider -= 1

    return string