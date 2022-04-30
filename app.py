import streamlit as st

from bbquote.lib import get_quote

quote, author = get_quote()  # assuming the function returns an author and a quote

f"{quote}, {author}"

