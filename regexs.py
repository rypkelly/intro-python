# Ryan Kelly (rpk2kn)

import re

nospace = re.compile(r"\S+")

quotation = re.compile(r'("\S)[^"]*(\S")')

twonum = re.compile(r"(-?[0-9]+(\.?[0-9]*)?)(\s|,|(,\s))(-?[0-9]+(\.?[0-9]*)?)")

likely_name = re.compile(r"(([A-Z]\.)|([A-Z]([a-z]+)))\s((([A-Z]([a-z]+))\s([A-Z]([a-z]+)))|([A-Z]([a-z]+))|(([A-Z]\.)"
                         r"\s([A-Z]([a-z]+))))")
