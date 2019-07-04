from flask import Flask, request
from pattern.en import conjugate,PRESENT,PAST,INFINITIVE,SG,PL,INDICATIVE,IMPERATIVE,PROGRESSIVE
from nltk.stem import PorterStemmer

#flask constructor called
app = Flask(__name__)

#telling which URL should call the associated function, here the '/' refers to home page itself
@app.route('/')

#flask api ready for both GET(sending unencrypted form of message) & POST(to receive contents from a html form) methods 
@app.route('/', methods=['GET', 'POST']) 


def form_example():
    if request.method == 'POST': #this block is only entered when the form is submitted
        word = request.form.get('word')   #getting the word entered in the form
        #INDICATIVE
        #1st person singular - I present, past, future
        i_firsti_pre = conjugate(verb=word, tense=PRESENT, person = 1, number = SG, mood= INDICATIVE)
        i_firsti_pas = conjugate(verb=word, tense=PAST, person = 1, number = SG, mood= INDICATIVE)
        i_firsti_fut = conjugate(verb=word, tense=INFINITIVE, person = 1, number = SG, mood= INDICATIVE)

        #1st person plural - we
        i_firstwe_pre = conjugate(verb=word, tense=PRESENT, person = 1, number = PL, mood= INDICATIVE)
        i_firstwe_pas = conjugate(verb=word, tense=PAST, person = 1, number = PL, mood= INDICATIVE)
        i_firstwe_fut = 'will ' + conjugate(verb=word, tense=INFINITIVE, person = 1, number = PL, mood= INDICATIVE)

        #2nd person - you
        i_sec_pre = conjugate(verb=word, tense=PRESENT, person = 2, number = SG, mood= INDICATIVE)
        i_sec_pas = conjugate(verb=word, tense=PAST, person = 2, number = SG, mood= INDICATIVE)
        i_sec_fut = 'will ' + conjugate(verb=word, tense=INFINITIVE, person = 2, number = SG, mood= INDICATIVE)

        #3rd person singular - he/she/it
        i_thirdit_pre = conjugate(verb=word, tense=PRESENT, person = 3, number = SG, mood= INDICATIVE)
        i_thirdit_pas = conjugate(verb=word, tense=PAST, person = 3, number = SG, mood= INDICATIVE)
        i_thirdit_fut = 'will ' + conjugate(verb=word, tense=INFINITIVE, person = 3, number = SG, mood= INDICATIVE)

        #3rd person plural - they
        i_thirdthey_pre =conjugate(verb=word, tense=PRESENT, person = 3, number = PL, mood= INDICATIVE)
        i_thirdthey_pas =conjugate(verb=word, tense=PAST, person = 3, number = PL, mood= INDICATIVE)
        i_thirdthey_fut ='will ' + conjugate(verb=word, tense=INFINITIVE, person = 3, number = PL, mood= INDICATIVE)

        #PERFECT
        #1st person singular - I present, past, future
        p_firsti_pre = 'have ' +conjugate(verb=word, tense = PAST, person = 1, number = SG, mood = INDICATIVE, aspect = PROGRESSIVE)
        p_firsti_pas = 'had ' +conjugate(verb=word, tense= PAST, person = 1, number = SG, mood = INDICATIVE, aspect = PROGRESSIVE)
        p_firsti_fut = 'will have ' +conjugate(verb=word, tense= PAST, person = 1, number = SG, mood = INDICATIVE, aspect = PROGRESSIVE)

        #1st person plural - we
        p_firstwe_pre = 'have '+conjugate(verb=word, tense=PAST, person = 1, number = PL, mood = INDICATIVE, aspect = PROGRESSIVE)
        p_firstwe_pas ='had '+conjugate(verb=word, tense=PAST, person = 1, number = PL, mood = INDICATIVE, aspect = PROGRESSIVE)
        p_firstwe_fut = 'will have '+conjugate(verb=word, tense=PAST, person = 1, number = PL, mood = INDICATIVE, aspect = PROGRESSIVE)

        #2nd person - you
        p_sec_pre = 'have '+conjugate(verb=word, tense=PAST, person = 2, number = SG, mood = INDICATIVE, aspect = PROGRESSIVE)
        p_sec_pas ='had '+conjugate(verb=word, tense=PAST, person = 2, number = SG, mood = INDICATIVE, aspect = PROGRESSIVE)
        p_sec_fut ='will have '+conjugate(verb=word, tense=PAST, person = 2, number = SG, mood = INDICATIVE, aspect = PROGRESSIVE)

        #3rd person singular - he/she/it
        p_thirdit_pre ='has '+conjugate(verb=word, tense=PAST, person = 3, number = SG, mood = INDICATIVE, aspect = PROGRESSIVE)
        p_thirdit_pas ='had '+conjugate(verb=word, tense=PAST, person = 3, number = SG, mood = INDICATIVE, aspect = PROGRESSIVE)
        p_thirdit_fut ='will have '+conjugate(verb=word, tense=PAST, person = 3, number = SG, mood = INDICATIVE, aspect = PROGRESSIVE)

        #3rd person plural - they
        p_thirdthey_pre ='have '+conjugate(verb=word, tense=PAST, person = 3, number = PL, mood = INDICATIVE, aspect = PROGRESSIVE)
        p_thirdthey_pas ='had '+conjugate(verb=word, tense=PAST, person = 3, number = PL, mood = INDICATIVE, aspect = PROGRESSIVE)
        p_thirdthey_fut = 'will have '+conjugate(verb=word, tense=PAST, person = 3, number = PL, mood = INDICATIVE, aspect = PROGRESSIVE)

        #CONTINUOUS 
        #1st person singular - I present, past, future
        c_firsti_pre = 'am '+conjugate(verb=word, person = 1, number = SG, aspect= PROGRESSIVE, mood= INDICATIVE)
        c_firsti_pas = 'was '+conjugate(verb=word,  person = 1, number = SG, aspect= PROGRESSIVE, mood= INDICATIVE)
        c_firsti_fut = 'will be '+conjugate(verb=word,  person = 1, number = SG, aspect= PROGRESSIVE, mood= INDICATIVE)

        #1st person plural - we
        c_firstwe_pre ='are '+conjugate(verb=word, person = 1, number = PL, aspect= PROGRESSIVE)
        c_firstwe_pas ='were '+conjugate(verb=word,  person = 1, number = PL, aspect= PROGRESSIVE)
        c_firstwe_fut ='will be '+conjugate(verb=word, person = 1, number = PL, aspect= PROGRESSIVE)

        #2nd person - you
        c_sec_pre ='are '+conjugate(verb=word,  person = 2, number = SG, aspect= PROGRESSIVE)
        c_sec_pas = 'were '+conjugate(verb=word,  person = 2, number = SG, aspect= PROGRESSIVE)
        c_sec_fut ='will be '+conjugate(verb=word, person = 2, number = SG, aspect= PROGRESSIVE)

        #3rd person singular - he/she/it
        c_thirdit_pre ='is '+conjugate(verb=word,  person = 3, number = SG, aspect= PROGRESSIVE)
        c_thirdit_pas ='was '+conjugate(verb=word, person = 3, number = SG, aspect= PROGRESSIVE)
        c_thirdit_fut ='will be '+conjugate(verb=word,  person = 3, number = SG, aspect= PROGRESSIVE)

        #3rd person plural - they
        c_thirdthey_pre ='are '+conjugate(verb=word,  person = 3, number = PL, aspect= PROGRESSIVE)
        c_thirdthey_pas ='were '+conjugate(verb=word,  person = 3, number = PL, aspect= PROGRESSIVE)
        c_thirdthey_fut ='will be '+conjugate(verb=word, person = 3, number = PL, aspect= PROGRESSIVE)

        #PERFECT CONTINUOUS
        #1st person singular - I present, past, future
        pc_firsti_pre = 'have been '+conjugate(verb=word, person = 1, number = SG, aspect= PROGRESSIVE, mood= INDICATIVE)
        pc_firsti_pas ='had been '+conjugate(verb=word,  person = 1, number = SG, aspect= PROGRESSIVE, mood= INDICATIVE)
        pc_firsti_fut ='will have been '+conjugate(verb=word,  person = 1, number = SG, aspect= PROGRESSIVE, mood= INDICATIVE)

        #1st person plural - we
        pc_firstwe_pre ='have been '+conjugate(verb=word, person = 1, number = PL, aspect= PROGRESSIVE)
        pc_firstwe_pas ='had been '+conjugate(verb=word,  person = 1, number = PL, aspect= PROGRESSIVE)
        pc_firstwe_fut ='will have been '+conjugate(verb=word, person = 1, number = PL, aspect= PROGRESSIVE)

        #2nd person - you
        pc_sec_pre ='have been '+conjugate(verb=word,  person = 2, number = SG, aspect= PROGRESSIVE)
        pc_sec_pas ='had been '+conjugate(verb=word,  person = 2, number = SG, aspect= PROGRESSIVE)
        pc_sec_fut ='will have been '+conjugate(verb=word, person = 2, number = SG, aspect= PROGRESSIVE)

        #3rd person singular - he/she/it
        pc_thirdit_pre ='has been '+conjugate(verb=word,  person = 3, number = SG, aspect= PROGRESSIVE)
        pc_thirdit_pas ='had been '+conjugate(verb=word, person = 3, number = SG, aspect= PROGRESSIVE)
        pc_thirdit_fut ='will have been '+conjugate(verb=word,  person = 3, number = SG, aspect= PROGRESSIVE)

        #3rd person plural - they
        pc_thirdth_pre ='have been '+conjugate(verb=word,  person = 3, number = PL, aspect= PROGRESSIVE)
        pc_thirdth_pas ='had been '+conjugate(verb=word,  person = 3, number = PL, aspect= PROGRESSIVE)
        pc_thirdth_fut ='will have been '+conjugate(verb=word, person = 3, number = PL, aspect= PROGRESSIVE)

        #printing out a html page of verb conjugations
        return '''<h2>Root form of {} is {}</h2>
                  <h2>INDICATIVE</h2>
                  <table>
                    <thead><tr><th>Person</th><th>Present</th><th>Past</th><th>Future</th></tr></thead>
                        <tbody>
                        <tr><td>I</td><td>{}</td><td>{}</td><td>{}</td></tr>
                        <tr><td>We</td><td>{}</td><td>{}</td><td>{}</td></tr>
                        <tr><td>You</td><td>{}</td><td>{}</td><td>{}</td></tr>
                        <tr><td>He/She/It</td><td>{}</td><td>{}</td><td>{}</td></tr>
                        <tr><td>They</td><td>{}</td><td>{}</td><td>{}</td></tr>
                        </tbody>
                  </table>

                  <h2>PERFECT TENSES</h2>
                  <table>
                    <thead><tr><th>Person</th><th>Present</th><th>Past</th><th>Future</th></tr></thead>
                        <tbody>
                        <tr><td>I</td><td>{}</td><td>{}</td><td>{}</td></tr>
                        <tr><td>We</td><td>{}</td><td>{}</td><td>{}</td></tr>
                        <tr><td>You</td><td>{}</td><td>{}</td><td>{}</td></tr>
                        <tr><td>He/She/It</td><td>{}</td><td>{}</td><td>{}</td></tr>
                        <tr><td>They</td><td>{}</td><td>{}</td><td>{}</td></tr>
                        </tbody>
                  </table>
                   <h2>CONTINUOUS TENSES</h2>
                  <table>

                    <thead><tr><th>Person</th><th>Present</th><th>Past</th><th>Future</th></tr></thead>
                        <tbody>
                        <tr><td>I</td><td>{}</td><td>{}</td><td>{}</td></tr>
                        <tr><td>We</td><td>{}</td><td>{}</td><td>{}</td></tr>
                        <tr><td>You</td><td>{}</td><td>{}</td><td>{}</td></tr>
                        <tr><td>He/She/It</td><td>{}</td><td>{}</td><td>{}</td></tr>
                        <tr><td>They</td><td>{}</td><td>{}</td><td>{}</td></tr>
                        </tbody>
                  </table>
                  
                  <h2>PERFECT CONTINUOUS TENSES</h2>
                  <table>

                    <thead><tr><th>Person</th><th>Present</th><th>Past</th><th>Future</th></tr></thead>
                        <tbody>
                        <tr><td>I</td><td>{}</td><td>{}</td><td>{}</td></tr>
                        <tr><td>We</td><td>{}</td><td>{}</td><td>{}</td></tr>
                        <tr><td>You</td><td>{}</td><td>{}</td><td>{}</td></tr>
                        <tr><td>He/She/It</td><td>{}</td><td>{}</td><td>{}</td></tr>
                        <tr><td>They</td><td>{}</td><td>{}</td><td>{}</td></tr>
                        </tbody>
                  </table>'''.format(word, word,i_firsti_pre,i_firsti_pas,i_firsti_fut,i_firstwe_pre,i_firstwe_pas,i_firstwe_fut,
                  i_sec_pre,i_sec_pas,i_sec_fut,i_thirdit_pre,i_thirdit_pas,i_thirdit_fut,i_thirdthey_pre,i_thirdthey_pas,
                  i_thirdthey_fut, p_firsti_pre,p_firsti_pas,p_firsti_fut,p_firstwe_pre,p_firstwe_pas,p_firstwe_fut,p_sec_pre,
                  p_sec_pas,p_sec_fut,p_thirdit_pre,p_thirdit_pas,p_thirdit_fut,p_thirdthey_pre,p_thirdthey_pas,p_thirdthey_fut,
                  c_firsti_pre,c_firsti_pas,c_firsti_fut,c_firstwe_pre,c_firstwe_pas,c_firstwe_fut,c_sec_pre,c_sec_pas,c_sec_fut,
                  c_thirdit_pre,c_thirdit_pas,c_thirdit_fut,c_thirdthey_pre,c_thirdthey_pas,c_thirdthey_fut,pc_firsti_pre,
                  pc_firsti_pas,pc_firsti_fut,pc_firstwe_pre,pc_firstwe_pas,pc_firstwe_fut,pc_sec_pre,pc_sec_pas,pc_sec_fut,
                  pc_thirdit_pre,pc_thirdit_pas,pc_thirdit_fut,pc_thirdth_pre,pc_thirdth_pas,pc_thirdth_fut                 
                  ) # {} to be replaced by the output variables from conjugate method
  
    #initial html form displayed for input
    return '''<form method="POST">
                  Word: <input type="text" name="word"><br>
                  <input type="submit" value="Submit"><br>
              </form>'''


#setting this particular module(source file) to run as the main program
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=True)  #running on local host on port 8000 debug true, to display debugging insights during development

    
