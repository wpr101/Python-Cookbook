from bottle import route, run

@route('/input')
def kmers_form():
    return '''
        <form action="/output" method="post">
            DNA: <input name="dna" type="text" /><br/>
            kmer length: <input name="kmer_length" type="text" /><br/>
            threshold: <input name="threshold" type="text" /><br/>
            <input value="Analyse" type="submit" />
        </form>
    '''

run(host='localhost', port=8080, debug=True)
