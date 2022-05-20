from flask import Flask, render_template, request
from jones_matrices import calculate_polarisation #type:ignore

app = Flask(__name__)


input_polarisation = 'Linear 45 Degrees'
element_order = []

@app.route("/", methods = ['POST','GET'])
def hello_world():
    
    if request.method == 'POST':
        
        if request.form.get('add') == 'Add':
            element_order.append(str(request.form.get("optics_select")))
            selected = (request.form.get('optics_select'))
            output,string = calculate_polarisation(element_order,input_polarisation)
            return render_template('index.html', lads = element_order,test = output, input_pol = input_polarisation,jones_calc = string)
        
        elif request.form.get('remove') == 'Remove':
            if len(element_order)>0:
                element_order.pop()
                output,string = calculate_polarisation(element_order,input_polarisation)
            else:
                output = r'\begin{bmatrix} 1 & 2 & 3\\ a & b & c \end{bmatrix}'
                string = 'blah'
            selected = (request.form.get('optics_select'))
            
            return render_template('index.html', lads = element_order,test = output, input_pol = input_polarisation,jones_calc = string)

            
    elif request.method == 'GET':
        return render_template('index.html', lads = element_order)


    

    return render_template("index.html")





