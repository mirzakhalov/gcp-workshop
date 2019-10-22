


# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# Instantiates a client
client = language.LanguageServiceClient()

# The text to analyze
type_ = enums.Document.Type.PLAIN_TEXT

# Optional. If not specified, the language is automatically detected.
# For list of supported languages:
# https://cloud.google.com/natural-language/docs/languages

text_en = "I am learning how to code today. This the best day of my life."
text_es = "He tenido un mal dia. Lloré dos veces. Mi perro murió."

document = {"content": text_en, "type": type_}

# Available values: NONE, UTF8, UTF16, UTF32
encoding_type = enums.EncodingType.UTF8

response = client.analyze_sentiment(document, encoding_type=encoding_type)
# Get overall sentiment of the input document
print(u"Document sentiment score: {}".format(response.document_sentiment.score))
print(
    u"Document sentiment magnitude: {}".format(
        response.document_sentiment.magnitude
    )
)
# Get sentiment for all sentences in the document
for sentence in response.sentences:
    print(u"Sentence text: {}".format(sentence.text.content))
    print(u"Sentence sentiment score: {}".format(sentence.sentiment.score))
    print(u"Sentence sentiment magnitude: {}".format(sentence.sentiment.magnitude))

# Get the language of the text, which will be the same as
# the language specified in the request or, if not specified,
# the automatically-detected language.
print(u"Language of the text: {}".format(response.language))
