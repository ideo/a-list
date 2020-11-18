'''
A simple streamlit app that checks how similar text is to 
  -how IDEO talks
  -how good IDEO leads talk
'''

import streamlit as st

def calculate_similarity(text, corpus):
    '''
    inputs:
    text- str, the text that will be compared
    corpus- str, the text to which the input text will be compared
    output:
    similarity- float, a score that describes how similar the text is to the corpus
    '''
    #TODO: Calculate similarity
    # This entire function will likely be it's own script somewhere
    similarity = .3
    return similarity


# Create the interface
st.title('Is this a good lead?')

st.text('Some explanatory text about what this tool does will go here. Blah Blah.')

st.header('Similarity Test')
st.text('Paste some text into the box below to see how similar it is to our IDEO corpus.')
test_text = st.text_input('Text')
comparison_corpus = st.selectbox(
    'To which corpus would you like to compare your text?',
    ('Transformational clients before they were transformational', 'IDEO Journal')
)

# Do the similarity calculations once user presses the button :)
if st.button('Compare!'):

    # Calculate similarity
    # TODO need to grab this code
    similarity = calculate_similarity(test_text, comparison_corpus)

    st.write('This text has a similarity score of {}'.format(similarity))
