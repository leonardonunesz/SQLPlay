// ===== JOGO DA VELHA - LÓGICA JAVASCRIPT =====

// Variáveis globais
let partidaAtiva = false;
let modoJogo = null;
let jogadorAtual = "X";
let tabuleiroData = {};

// Função para selecionar modo de jogo
function selecionarModo(modo) {
    modoJogo = modo;

    // Marcar botão selecionado
    document
        .querySelectorAll(".mode-button")
        .forEach((btn) => btn.classList.remove("active"));
    event.target.classList.add("active");

    // Ocultar seleção de modo
    document.getElementById("modeSelection").classList.add("hidden");

    // Mostrar elementos do jogo
    document.getElementById("gameInfo").classList.remove("hidden");
    document.getElementById("gameBoard").classList.remove("hidden");
    document.getElementById("sqlSection").classList.remove("hidden");

    // Atualizar status do jogo
    if (modo === "single") {
        document.getElementById("gameStatus").textContent =
            "Você é o X, o computador é o O";
    } else {
        document.getElementById("gameStatus").textContent =
            "Jogador X vs Jogador O - Use comandos SQL para jogar";
    }

    // Iniciar novo jogo
    iniciarNovoJogo(modo);
}

// Função para iniciar novo jogo
function iniciarNovoJogo(modo) {
    fetch('/jogo-da-velha/novo-jogo/', {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ modo: modo }),
    })
        .then((response) => response.json())
        .then((data) => {
            if (data.success) {
                // Resetar interface
                partidaAtiva = true;
                modoJogo = data.modo_jogo;
                jogadorAtual = data.jogador_atual;

                // Atualizar tabuleiro
                atualizarTabuleiro(data.tabuleiro);

                // Atualizar informações
                document.getElementById(
                    "currentPlayer"
                ).textContent = `Vez do Jogador ${jogadorAtual}`;

                // Ocultar modal de resultado se estiver visível
                document.getElementById("resultModal").classList.add("hidden");
                document.getElementById("messageContainer").innerHTML = "";

                mostrarMensagem("Jogo iniciado!", "success");
            } else {
                mostrarMensagem(data.error, "error");
            }
        })
        .catch((error) => {
            mostrarMensagem(
                "Erro ao iniciar novo jogo: " + error.message,
                "error"
            );
        });
}

// Função para inicializar tabuleiro
function inicializarTabuleiro() {
    // Limpar tabuleiro
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            const cell = document.getElementById(`cell_${i}_${j}`);
            const span = cell.querySelector("span");
            span.textContent = "";
            cell.className = "cell";
        }
    }
}

// Função para executar comando SQL
function executarSQL() {
    const comando = document.getElementById("sqlInput").value.trim();

    if (!comando) {
        mostrarMensagem("Por favor, digite um comando SQL válido.", "error");
        return;
    }

    // Desabilitar botão durante execução
    const botao = document.querySelector(".execute-button");
    botao.disabled = true;
    botao.innerHTML =
        '<i class="fas fa-spinner fa-spin"></i> Executando...';

    fetch('/jogo-da-velha/executar-sql/', {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ comando: comando }),
    })
        .then((response) => response.json())
        .then((data) => {
            if (data.success) {
                mostrarMensagem(data.message, "success");

                // Atualizar tabuleiro
                if (data.tabuleiro) {
                    atualizarTabuleiro(data.tabuleiro);
                }

                // Atualizar jogador atual
                if (data.jogador_atual) {
                    jogadorAtual = data.jogador_atual;
                    document.getElementById(
                        "currentPlayer"
                    ).textContent = `Vez do Jogador ${jogadorAtual}`;
                }

                // Verificar se o jogo terminou
                if (data.jogo_finalizado) {
                    partidaAtiva = false;
                    mostrarResultado(data);
                }

                // Limpar input
                document.getElementById("sqlInput").value = "";
            } else {
                mostrarMensagem(data.error, "error");
            }
        })
        .catch((error) => {
            mostrarMensagem(
                "Erro ao executar comando SQL: " + error.message,
                "error"
            );
        })
        .finally(() => {
            // Reabilitar botão
            botao.disabled = false;
            botao.innerHTML = '<i class="fas fa-play"></i> Executar SQL';
        });
}

// Função para atualizar tabuleiro
function atualizarTabuleiro(tabuleiroData) {
    // Limpar tabuleiro
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            const cell = document.getElementById(`cell_${i}_${j}`);
            const span = cell.querySelector("span");
            span.textContent = "";
            cell.className = "cell";
        }
    }

    // Preencher com novos dados
    Object.keys(tabuleiroData).forEach((key) => {
        const [linha, coluna] = key.split("_");
        const valor = tabuleiroData[key];
        const cell = document.getElementById(`cell_${linha}_${coluna}`);
        const span = cell.querySelector("span");
        span.textContent = valor;
        cell.classList.add(valor.toLowerCase());
    });
}

// Função para mostrar resultado do jogo
function mostrarResultado(data) {
    const modal = document.getElementById("resultModal");
    const title = document.getElementById("modalTitle");
    const message = document.getElementById("modalMessage");

    if (data.empate) {
        title.textContent = "🏆 Empate!";
        message.textContent =
            "O jogo terminou em empate. Escolha como quer jogar novamente:";
    } else if (data.vencedor) {
        title.textContent = "🎉 Fim de Jogo!";
        message.textContent = `Jogador ${data.vencedor} venceu! Escolha como quer jogar novamente:`;
    }

    modal.classList.remove("hidden");
}

// Função para jogar novamente
function jogarNovamente(modo) {
    // Ocultar modal de resultado
    document.getElementById("resultModal").classList.add("hidden");

    // Iniciar novo jogo
    iniciarNovoJogo(modo);
}

// Função para mostrar modal de ajuda
function mostrarAjuda() {
    document.getElementById("helpModal").classList.remove("hidden");
}

// Função para ocultar modal de ajuda
function ocultarAjuda() {
    document.getElementById("helpModal").classList.add("hidden");
}

// Função para mostrar mensagens
function mostrarMensagem(mensagem, tipo) {
    const container = document.getElementById("messageContainer");
    const messageDiv = document.createElement("div");
    messageDiv.className =
        tipo === "error" ? "error-message" : "success-message";
    messageDiv.innerHTML = `<i class="fas fa-${
        tipo === "error" ? "exclamation-triangle" : "check-circle"
    }"></i> ${mensagem}`;

    container.appendChild(messageDiv);

    // Remover mensagem após 5 segundos
    setTimeout(() => {
        messageDiv.remove();
    }, 5000);
}

// ===== INICIALIZAÇÃO =====

// Event listener para quando o DOM estiver carregado
document.addEventListener("DOMContentLoaded", function () {
    // Permitir executar SQL com Enter
    const sqlInput = document.getElementById("sqlInput");
    if (sqlInput) {
        sqlInput.addEventListener("keypress", function (e) {
            if (e.key === "Enter") {
                executarSQL();
            }
        });
    }

    // Fechar modais clicando fora deles
    document.addEventListener("click", function (e) {
        if (e.target.classList.contains("modal-overlay")) {
            document.getElementById("resultModal").classList.add("hidden");
        }
        if (e.target.classList.contains("help-modal-overlay")) {
            document.getElementById("helpModal").classList.add("hidden");
        }
    });
});
