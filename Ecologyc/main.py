from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# Código da parte de pontos
usuario_pontos = 330

@app.route('/calculo', methods=['POST'])
def calculo():
    valores_selecionados = request.form.getlist('checkbox')
    
    if valores_selecionados:
        soma = sum(int(valor) for valor in valores_selecionados)
    else:
        soma = 0
    
    return render_template('resultado.html', soma=soma)

@app.route('/confirmar_resgate', methods=['POST'])
def confirmar_resgate():
    premio = request.form.get('premio')
    pontos = int(request.form.get('pontos'))
    pontos_restantes = int(request.form.get('pontos_restantes'))

    global usuario_pontos
    if usuario_pontos >= pontos: 
        usuario_pontos -= pontos  
        mensagem = f"Você resgatou o prêmio '{premio}' com {pontos} pontos. Entraremos em contato em seu email em breve. Seus pontos restantes: {usuario_pontos}."
    else:
        mensagem = f"Você não tem pontos suficientes para resgatar o prêmio '{premio}'. Seus pontos: {usuario_pontos}."

    return render_template('resultado.html', mensagem=mensagem, soma=usuario_pontos)

# Código da parte de Donate
@app.route('/donate', methods=['POST'])
def process_donation():
    amount = request.form.get('amount')
    custom_amount = request.form.get('customAmount')

    if amount == "other" and custom_amount:
        donation_value = custom_amount
    elif amount:
        donation_value = amount
    else:
        donation_value = "Valor não especificado"

    print(f"Valor da doação recebido: R$ {donation_value}")
    
    return render_template('donation.html', donation_value=donation_value)

# Código da parte de Contato
@app.route('/submit', methods=['POST'])
def submit_contact():
    name = request.form.get('name')
    email = request.form.get('email')
    subject = request.form.get('subject')
    message = request.form.get('message')

    print(f"Nome: {name}")
    print(f"E-mail: {email}")
    print(f"Assunto: {subject}")
    print(f"Mensagem: {message}")

    return render_template('confirmation.html', name=name, subject=subject)

if __name__ == "__main__":
    app.run(debug=True)
