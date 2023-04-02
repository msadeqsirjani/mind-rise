import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from src.text_cleaning.core import *


def draw(df: pd.DataFrame) -> None:
    df = df.head(n=10)
    for index, row in df.iterrows():
        text = ' '.join(row['extracted_keywords'].split())
        wordcloud = WordCloud(width=800,
                              height=800,
                              background_color='white',
                              min_font_size=10,
                              colormap='Set2').generate(text)
        wordcloud.to_file(f"../result/images/word_cloud_{index}.png")


# draw(df=pre_process(df=data_frame))
