from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    reply=""
    if 'symbol' in request.args:
        reply="hi"
        name = request.args['symbol']
        if name == 'Alabama':
            reply = "Na"
        elif name == 'Alaska':
            reply = "yo"""

            
            
    return render_template('home.html', response = reply)
   

@app.route("/page1")
def render_page1():
    reply=""
    if 'symbol' in request.args:
        reply="try again!"
        name = request.args['symbol']
        if name == 'Arizona':
            reply = "yo"""
        elif name == 'Arkansas':
            reply = "yo"""
        elif name == 'California':
            reply = "yo"""
        elif name == 'Colorado':
            reply = "yo"""
        elif name == 'Connecticut':
            reply = "yo"""
        elif name == 'Delaware':
            reply = "yo"""
        elif name == 'Florida':
            reply = "yo"""
        elif name == 'Georgia':
            reply = "yo"""
        elif name == 'Hawaii':
            reply = "yo"""
        elif name == 'Idaho':
            reply = "yo"""
        elif name == 'Illinios':
            reply = "yo""
        elif name == 'Indiana':
            reply = "yo"""
        elif name == 'Iowa':
            reply = "yo"""
        elif name == 'Kansas':
            reply = "yo"""
        elif name == 'Kentucky':
            reply = "yo"""
        elif name == 'Louisiana':
            reply = "yo"""
        elif name == 'Maine':
            reply = "yo"""
        elif name == 'Maryland':
            reply = "yo"""
        elif name == 'Massachusetts':
            reply = "yo"""
        elif name == 'Michigan':
            reply = "yo"""
        elif name == 'Minnesota':
            reply = "yo"""
        elif name == 'Mississippi':
            reply = "yo"""
        elif name == 'Missouri':
            reply = "yo"""
        elif name == 'Montana':
            reply = "yo"""
        elif name == 'Nebraska':
            reply = "yo"""
        elif name == 'Nevada':
            reply = "yo"""
        elif name == 'New Hampshire':
            reply = "yo"""
        elif name == 'New Jersey':
            reply = "yo"""
        elif name == 'New Mexico':
            reply = "yo"""
        elif name == 'New York':
            reply = "yo"""
        elif name == 'North Carolina':
            reply = "yo"""
        elif name == 'North Dakota':
            reply = "yo"""
        elif name == 'Ohio':
            reply = "yo"""
        elif name == 'Oklahoma':
            reply = "yo"""
        elif name == 'Oregon':
            reply = "yo"""
        elif name == 'Pennsylvania':
            reply = "yo"""
        elif name == 'Rhode Island':
            reply = "yo"""
        elif name == 'South Carolina':
            reply = "yo"""
        elif name == 'South Dakota':
            reply = "yo"""
        elif name == 'Tennessee':
            reply = "yo"""
        elif name == 'Texas':
            reply = "yo"""
        elif name == 'Utah':
            reply = "yo"""
        elif name == 'Vermont':
            reply = "yo"""
        elif name == 'Virginia':
            reply = "yo"""
        elif name == 'Washington':
            reply = "yo"""
        elif name == 'West Virginia':
            reply = "yo"""
        elif name == 'Wisconsin':
            reply = "yo"""
        elif name == 'Wyoming':
            reply = "yo"""
    return render_template('page1.html', response = reply)
    
    

@app.route("/page2")
def render_page2():
    reply=""
    if 'symbol' in request.args:
        name = request.args['symbol']   
        if name == 'Genitourinary':
             reply = "C"
        elif name == 'Eye':
             reply = "S"
        elif name == 'Nervous System':
             reply = "S"                
        elif name == 'Musculoskeletal':
             reply = "S"    
        elif name == 'Skin':
             reply = "S"    
         elif name == 'Gastrointestinal':
             reply = "S"    
         elif name == 'Cardiovascular':
             reply = "S"    
    return render_template('page2.html', response = reply)
    
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
