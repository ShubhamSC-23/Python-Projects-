import pandas

nato_alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")  

nato_alphabet_dict = {
    row.letter: row.code for (index, row) in nato_alphabet_df.iterrows()
}
user_answer = input("Enter a word: ").upper()  
answer_list = [nato_alphabet_dict[letter] for letter in user_answer if letter != " "]  
print(answer_list)



letter,code
A,Alfa
B,Bravo
C,Charlie
D,Delta
E,Echo
F,Foxtrot
G,Golf
H,Hotel
I,India
J,Juliet
K,Kilo
L,Lima
M,Mike
N,November
O,Oscar
P,Papa
Q,Quebec
R,Romeo
S,Sierra
T,Tango
U,Uniform
V,Victor
W,Whiskey
X,X-ray
Y,Yankee
Z,Zulu