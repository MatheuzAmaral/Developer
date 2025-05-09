<!DOCTYPE html><html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Inventário de Caixas de Incêndio</title>
  <style>
    * { box-sizing: border-box; }
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      background: #f4f4f4;
    }
    header {
      background: #b71c1c;
      color: white;
      padding: 1rem;
      text-align: center;
    }
    .controls {
      padding: 1rem;
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      justify-content: center;
    }
    select, input[type="text"], button {
      padding: 10px;
      border-radius: 5px;
      border: 1px solid #ccc;
      font-size: 1rem;
    }
    .inventory-item {
      background: white;
      margin: 10px;
      padding: 15px;
      border-radius: 8px;
      box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    .inventory-item h2 {
      margin-top: 0;
      color: #d32f2f;
    }
    .inventory-item p {
      margin: 5px 0;
    }
  </style>
</head>
<body>  <header>
    <h1>Inventário de Caixas de Incêndio</h1>
  </header>  <div class="controls">
    <input type="text" id="search" placeholder="Buscar por número, extintor, etc..." />
    <select id="filter-month">
      <option value="">Mês</option>
    </select>
    <select id="filter-year">
      <option value="">Ano</option>
    </select>
    <button onclick="clearFilters()">Limpar Filtros</button>
    <button onclick="addNewBox()">Nova Caixa</button>
    <button onclick="exportCSV()">Exportar CSV</button>
  </div>  <main id="inventory-list"></main>  <script>
    let inventory = JSON.parse(localStorage.getItem('inventory')) || [
      {
        numero: "Cx 1",
        status: "ok",
        extintores: ["ABC 02871 (03/25)", "CO2 18140 (03/25)"],
        mangueiras: ["07/25", "08/25"],
        observacao: "Esguicho rígido, chave ok."
      },
      {
        numero: "Cx 2",
        status: "ok",
        extintores: ["ABC 06046 (03/25)"],
        mangueiras: ["07/25", "08/25"],
        observacao: "Placas não precisam ser trocadas."
      }
    ];

    const months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"];
    const years = ["24", "25", "26", "27", "28"];

    function populateFilters() {
      const monthSelect = document.getElementById("filter-month");
      const yearSelect = document.getElementById("filter-year");
      months.forEach(m => monthSelect.innerHTML += `<option value="${m}">${m}</option>`);
      years.forEach(y => yearSelect.innerHTML += `<option value="${y}">${y}</option>`);
    }

    function renderInventory(filter = "") {
      const list = document.getElementById("inventory-list");
      list.innerHTML = "";

      const month = document.getElementById("filter-month").value;
      const year = document.getElementById("filter-year").value;

      inventory
        .filter(item => {
          const combined = `${item.numero} ${item.extintores.join(" ")} ${item.observacao}`.toLowerCase();
          const matchesText = combined.includes(filter.toLowerCase());

          const matchesExt = item.extintores.some(ext => ext.includes(`(${month}/${year})`));
          const matchesMang = item.mangueiras.some(man => man === `${month}/${year}`);
          const matchesDate = (!month && !year) || matchesExt || matchesMang;

          return matchesText && matchesDate;
        })
        .forEach(item => {
          const div = document.createElement("div");
          div.className = "inventory-item";
          div.innerHTML = `
            <h2>${item.numero} - ${item.status}</h2>
            <p><strong>Extintores:</strong> ${item.extintores.join(", ")}</p>
            <p><strong>Mangueiras:</strong> ${item.mangueiras.join(", ")}</p>
            <p><strong>Observação:</strong> ${item.observacao}</p>
          `;
          list.appendChild(div);
        });
    }

    document.getElementById("search").addEventListener("input", (e) => {
      renderInventory(e.target.value);
    });

    document.getElementById("filter-month").addEventListener("change", () => renderInventory(document.getElementById("search").value));
    document.getElementById("filter-year").addEventListener("change", () => renderInventory(document.getElementById("search").value));

    function clearFilters() {
      document.getElementById("search").value = "";
      document.getElementById("filter-month").value = "";
      document.getElementById("filter-year").value = "";
      renderInventory();
    }

    function addNewBox() {
      const numero = prompt("Número da nova caixa:");
      if (!numero) return;

      const status = prompt("Status da nova caixa:", "ok");
      const extintores = prompt("Extintores (separados por vírgula):").split(",").map(s => s.trim());
      const mangueiras = prompt("Mangueiras (separadas por vírgula):").split(",").map(s => s.trim());
      const observacao = prompt("Observações:");

      inventory.push({ numero, status, extintores, mangueiras, observacao });
      localStorage.setItem("inventory", JSON.stringify(inventory));
      renderInventory();
    }

    function exportCSV() {
      let csv = "Número,Status,Extintores,Mangueiras,Observação\n";
      inventory.forEach(item => {
        csv += `"${item.numero}","${item.status}","${item.extintores.join(" - ")}","${item.mangueiras.join(" - ")}","${item.observacao}"\n`;
      });
      const blob = new Blob([csv], { type: "text/csv" });
      const link = document.createElement("a");
      link.href = URL.createObjectURL(blob);
      link.download = "inventario_caixas.csv";
      link.click();
    }

    window.onload = () => {
      populateFilters();
      renderInventory();
    }
  </script></body>
</html>