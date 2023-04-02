import config
import time
from src.text_cleaning.core import *

applications = pre_process(df=data_frame)

university = input("🎓 Give me the name of university. \n")
major = input('♾️ GIve me the name of you major. \n')
keywords = input('🔑 Give me the keywords related to this topic in comma separated form. \n')

reserved_keywords = applications.loc[applications['university_name'].str.contains(university) &
                                     applications['program_name'].str.contains(major)].head(n=1)["extracted_keywords"]

keywords = str(keywords + reserved_keywords.values).split(", ")

from src.crawler.gomoonbeam import *

sign_in(url=config.SIGN_IN_URL,
        email=config.EMAIL,
        password=config.PASSWORD)

navigate_user_to_templates(config.TEMPLATE_URL)

select_essay_writer()

fill_essay_with_custom_input_step_1(title=university,
                                    description=major,
                                    keywords=keywords)

fill_essay_with_custom_input_step_2()

fill_essay_with_custom_input_step_3()

fill_essay_with_custom_input_step_4()
