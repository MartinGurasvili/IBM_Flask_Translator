"""
translation modules from ibm watson ai
"""
import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
import urllib3
from xml.etree.ElementTree import VERSION

urllib3.disable_warnings()

VERSION = '2018-05-01'

load_dotenv()

APIKEY = os.environ['apikey']

URL = os.environ['url']



authenticator = IAMAuthenticator(APIKEY)
language_translator = LanguageTranslatorV3(
    version=VERSION,
    authenticator=authenticator
)

language_translator.set_service_url(URL)
language_translator.set_disable_ssl_verification(True)

def english_to_french(english_text):
    """
    translates english text to french
    """
    if english_text is None:
        return "Nothing to translate"
    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    french_text = translation.get("translations")[0].get("translation")
    return french_text


def french_to_english(french_text):
    """
    translates french text to english
    """
    if french_text is None:
        return "Nothing to translate"
    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    english_text = translation.get("translations")[0].get("translation")
    return english_text


