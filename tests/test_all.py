from tests.test_text_box_negative import test_negative
from tests.test_text_box import test_text_box_latin
from tests.test_kirill_text_box import test_kirill

def run_all():
    test_kirill()
    test_negative()
    test_text_box_latin()

if __name__ == "__main__":
    run_all()