let pedido = [];
let total = 0;

function adicionarProduto(nome, preco) {
    pedido.push({ nome, preco });
    total += preco;
    atualizarPedido();
}

function atualizarPedido() {
    const lista = document.getElementById('lista-pedido');
    lista.innerHTML = '';

    pedido.forEach(item => {
        const li = document.createElement('li');
        li.textContent = `${item.nome} - R$${item.preco.toFixed(2)}`;
        lista.appendChild(li);
    });

    document.getElementById('total').textContent = total.toFixed(2);
}

function finalizarPedido() {
    const formaPagamento = document.getElementById('forma-pagamento').value;
    if (pedido.length === 0) {
        alert('Seu pedido está vazio!');
        return;
    }

    alert(`Pedido finalizado!\nTotal: R$${total.toFixed(2)}\nForma de pagamento: ${formaPagamento.toUpperCase()}`);

    // Limpar o pedido
    pedido = [];
    total = 0;
    atualizarPedido();
}
