def Texts(text,lang):
    if translatedTexts.get(text) is not None:
        textDict = translatedTexts.get(text)
        return textDict.get(lang)
    return text


translatedTexts = {
    "INVALID_INFORMATION":{
        "en":"The Information you have requested is not permitted for public request.",
        "hi":"जानकारी जो आप अनुरोध किया है जनता के अनुरोध के लिए अनुमति नहीं है।",
        "mr":"The Information you have requested is not permitted for public request.",
        "ta":"The Information you have requested is not permitted for public request.",
        "te":"The Information you have requested is not permitted for public request.",
    },
    "INSTANCE_TOKEN_MISMATCH":{
        "en":"Sorry, there is some problem in displaying the page. Please logout and login again for better experience.",
        "hi":"Sorry, there is some problem in displaying the page. Please logout and login again for better experience.",
        "mr":"Sorry, there is some problem in displaying the page. Please logout and login again for better experience.",
        "ta":"Sorry, there is some problem in displaying the page. Please logout and login again for better experience.",
        "te":"Sorry, there is some problem in displaying the page. Please logout and login again for better experience.",
    },
    }