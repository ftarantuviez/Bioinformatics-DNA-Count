import pandas as pd
import streamlit as st
import altair as alt


st.set_page_config(page_title='Bioinformatics DNA Count', page_icon="./f.png")

st.write(""" 
# DNA Nucleotide Count Web App

This app counts the nucleotide composition of query DNA!
""")

st.header('Enter DNA Sequence')

sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

sequence = st.text_area("Sequence Input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = ''.join(sequence)

st.write("""
***
""")

st.header('INPUT (DNA Query)')

st.header('OUTPUT (DNA Nucleotide Count)')

# 1. Print count of each nucleotide
st.subheader('1. Print dictionary')

def DNA_nucleotide_count(seq):
  d = dict([
    ('A', seq.count('A')),
    ('T', seq.count('T')),
    ('G', seq.count('G')),
    ('C', seq.count('C')),
  ])
  return d

X = DNA_nucleotide_count(sequence)
X_label = list(X)
X_values = list(X.values())

X

# 2. Print the text
st.subheader('2. Print text')
st.write('There are ' + str(X['A']) + ' adenine (A)')
st.write('There are ' + str(X['T']) + ' thymine (T)')
st.write('There are ' + str(X['G']) + ' guanine (G)')
st.write('There are ' + str(X['C']) + ' cytosine (C)')

# 3. Display dataframe
st.subheader('3. Display Dataframe')
df = pd.DataFrame.from_dict(X, orient="index")
df = df.rename({0: "count"}, axis=1)
df.reset_index(inplace=True)
df = df.rename(columns={"index": "nucleotide"})
st.write(df)

# 4. Display Bar Chart using Altair
st.subheader('4. Display Bar Chart')
p = alt.Chart(df).mark_bar().encode(
  x='nucleotide',
  y='count'
)
p = p.properties(
  width=alt.Step(80)
)
st.write(p)

st.write("""
  ## App repository

  [Github](https://github.com/ftarantuviez/Bioinformatics-DNA-Count)
""")

