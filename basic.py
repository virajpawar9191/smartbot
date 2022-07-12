from pywikihow import search_wikihow
from speak import Speak 
# 5. Basic Topics info


def basicque(task):

    max_result = 1
    how_to_func = search_wikihow(task, max_result)
    assert len(how_to_func) == 1
    how_to_func[0].print()
    Speak(how_to_func[0].summary)




