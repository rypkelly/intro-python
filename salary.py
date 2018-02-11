# Ryan Kelly (rpk2kn)

import re
import urllib.request

def get_info(name):
    info = dict()

    reg1 = re.compile(r"(([A-Z][a-z]+(-[A-Z][a-z]+)*) )+([A-Z][a-z]+(-[A-Z][a-z]+)*)")
    reg2 = re.compile(r"([A-Z][a-z]+(-[A-Z][a-z]+)*),( ([A-Z][a-z]+(-[A-Z][a-z]+)*))+")
    reg3 = re.compile(r"[a-z]+(-[a-z]+)+")
    reg4 = re.compile(r"[0-9]+")
    match1 = reg1.search(name)
    match2 = reg2.search(name)
    match3 = reg3.search(name)
    match4 = reg4.search(name)
    if match2:
        normalized = match2.group(0).lower().split(" ")
        blank = ""
        for word in range(1, len(normalized)):
            blank += normalized[word]
            blank += "-"
        blank += str(normalized[0]).strip(",")
        normalized = blank
    elif match1:
        normalized = match1.group(0).lower().split(" ")
        blank = ""
        for word in range(len(normalized)-1):
            blank += normalized[word]
            blank += "-"
        blank += normalized[-1]
        normalized = blank
    elif match3:
        normalized = match3.group(0)
    else:
        normalized = match4.group(0)
    url = "http://cs1110.cs.virginia.edu/files/uva2015/" + normalized
    try:
        stream = urllib.request.urlopen(url).read().decode("UTF-8")
    except:
        return info

    title_reg = re.compile(r"(Job title: )(.+)<")
    title_match = title_reg.search(stream)
    if title_match:
        title = title_match.group(2)
        if "&amp;" in title:
            title = title[:title.index("&amp;")] + "&" + title[title.index("&amp;") + 5:]
        if "&lt;" in title:
            title = title[:title.index("&lt;")] + "<" + title[title.index("&lt;") + 4:]
        if "&amp;" in title:
            title = title[:title.index("&gt;")] + ">" + title[title.index("&gt;") + 4:]
        info["title"] = title

    pay_reg = re.compile(r"(\(paytype\.amount, )([0-9]+\.[0-9]+)")
    pay_match = pay_reg.search(stream)
    if pay_match:
        pay = float(pay_match.group(2))
        info["pay"] = pay

    rank_reg = re.compile(r"(<td>)([0-9]+)(,?)([0-9]*) of 7,474</td>")
    rank_match = rank_reg.search(stream)
    if rank_match:
        rank = int(rank_match.group(2) + rank_match.group(4))
        info["rank"] = rank

    breakdown = dict()

    base_reg = re.compile(r"(\'Base salary\', 'amount': )([0-9]+(\.[0-9]+)?)")
    base_match = base_reg.search(stream)
    if base_match:
        base = float(base_match.group(2))
        breakdown["Base salary"] = base

    additional_reg = re.compile(r"(\'Additional compensation\', 'amount': )([0-9]+(\.[0-9]+)?)")
    additional_match = additional_reg.search(stream)
    if additional_match:
        additional = float(additional_match.group(2))
        breakdown["Additional compensation"] = additional

    non_state_reg = re.compile(r"(\'Non-state salary\', 'amount': )([0-9]+(\.[0-9]+)?)")
    non_state_match = non_state_reg.search(stream)
    if non_state_match:
        non_state = float(non_state_match.group(2))
        breakdown["Non-state salary"] = non_state

    deferred_reg = re.compile(r"(\'Deferred compensation\', 'amount': )([0-9]+(\.[0-9]+)?)")
    deferred_match = deferred_reg.search(stream)
    if deferred_match:
        deferred = float(deferred_match.group(2))
        breakdown["Deferred compensation"] = deferred

    info["breakdown"] = breakdown

    return info
