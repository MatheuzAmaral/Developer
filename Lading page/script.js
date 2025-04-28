// Variáveis para controle do pedido
let pedido = [];
let total = 0;

// Dados das categorias e produtos
const categorias = {
    hamburgueres: [
        { nome: 'Hambúrguer de Carne', preco: 20, imagem: 'imagens/hamburguer-carne.png' },
        { nome: 'Hambúrguer de Frango', preco: 18, imagem: 'imagens/hamburguer-frango.png' },
        { nome: 'Hambúrguer Vegetariano', preco: 22, imagem: 'imagens/hamburguer-veg.png' },
        { nome: 'Hambúrguer Duplo', preco: 25, imagem: 'imagens/hamburguer-duplo.png' },
    ],
    sorvetes: [
        { nome: 'Sorvete de Chocolate', preco: 10, imagem: 'imagens/sorvete-chocolate.png' },
        { nome: 'Sorvete de Morango', preco: 10, imagem: 'imagens/sorvete-morango.png' },
        { nome: 'Sorvete de Baunilha', preco: 10, imagem: 'imagens/sorvete-baunilha.png' },
        { nome: 'Sorvete de Pistache', preco: 12, imagem: 'imagens/sorvete-pistache.png' },
    ],
    refrigerantes: [
        { nome: 'Coca-Cola', preco: 8, imagem: 'imagens/coca-cola.png' },
        { nome: 'Guaraná', preco: 8, imagem: 'imagens/guarana.png' },
        { nome: 'Fanta Laranja', preco: 8, imagem: 'imagens/fanta-laranja.png' },
        { nome: 'Sprite', preco: 8, imagem: 'imagens/sprite.png' },
    ]
};

// Função para mostrar os produtos de uma categoria
function mostrarProdutos(categoria) {
    const produtosDiv = document.getElementById('produtos');
    produtosDiv.innerHTML = '';

    categorias[categoria].forEach(produto => {
        const div = document.createElement('div');
        div.className = 'produto';
        div.innerHTML = `
            <img src="${produto.imagem}" alt="${produto.nome}">
            <h3>${produto.nome}</h3>
            <p>R$${produto.preco.toFixed(2)}</p>
            <button onclick="adicionarProduto('${produto.nome}', ${produto.preco})">Adicionar</button>
        `;
        produtosDiv.appendChild(div);
    });
}

// Função para adicionar produto ao pedido
function adicionarProduto(nome, preco) {
    pedido.push({ nome, preco });
    total += preco;
    atualizarPedido();
}

// Atualizar o pedido na tela
function atualizarPedido() {
    const lista = document.getElementById('lista-pedido');
    lista.innerHTML = '';

    pedido.forEach((item, index) => {
        const li = document.createElement('li');
        li.innerHTML = `
            ${item.nome} - R$${item.preco.toFixed(2)}
            <button class="remover" onclick="removerItem(${index})">❌</button>
        `;
        lista.appendChild(li);
    });

    document.getElementById('total').textContent = total.toFixed(2);
}

// Função para remover um item
function removerItem(index) {
    total -= pedido[index].preco;
    pedido.splice(index, 1);
    atualizarPedido();
}

// Finalizar o pedido
function finalizarPedido() {
    const formaPagamento = document.getElementById('forma-pagamento').value;
    if (pedido.length === 0) {
        alert('Seu pedido está vazio!');
        return;
    }

    alert(`Pedido finalizado!\nTotal: R$${total.toFixed(2)}\nForma de pagamento: ${formaPagamento.toUpperCase()}`);

    // Resetar pedido
    pedido = [];
    total = 0;
    atualizarPedido();
}
