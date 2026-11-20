/**
 * Treeal Corp - Scripts Globais & Efeitos Visuais Interativos (Frontend Agent)
 */

async function carregarStatusAPIs() {
    const container = document.getElementById('listaApiStatus');
    const icone = document.getElementById('iconeRefresh');
    if (icone) icone.classList.add('fa-spin');

    try {
        const response = await fetch("/api/status/");
        const data = await response.json();

        let html = '';
        data.apis.forEach(api => {
            let corDot = 'bg-emerald-400';
            let textoStatus = 'Online';
            let corTexto = 'text-emerald-300';

            if (api.status === 'rate-limit') {
                corDot = 'bg-amber-400';
                textoStatus = 'Rate Limit';
                corTexto = 'text-amber-300';
            } else if (api.status === 'offline') {
                corDot = 'bg-red-500';
                textoStatus = 'Offline';
                corTexto = 'text-red-400';
            }

            html += `
                <div class="flex items-center justify-between text-xs bg-white/5 px-3 py-2 rounded-xl border border-white/5">
                    <span class="font-medium text-slate-300">${api.nome}</span>
                    <div class="flex items-center space-x-1.5">
                        <span class="w-2 h-2 rounded-full ${corDot} animate-pulse"></span>
                        <span class="${corTexto} text-[10px] font-bold">${textoStatus}</span>
                    </div>
                </div>
            `;
        });
        if (container) container.innerHTML = html;
    } catch (e) {
        if (container) container.innerHTML = `<div class="text-xs text-red-400 py-1 text-center">Erro ao checar status</div>`;
    } finally {
        if (icone) icone.classList.remove('fa-spin');
    }
}

function copiarTextoMensagem() {
    const textarea = document.getElementById('textoCopiaEquipe');
    if (!textarea) return;

    textarea.select();
    textarea.setSelectionRange(0, 99999);
    navigator.clipboard.writeText(textarea.value).then(() => {
        const btn = document.getElementById('textoBotaoCopiar');
        if (btn) {
            btn.innerHTML = '<i class="fa-solid fa-check mr-1"></i> Copiado com Sucesso!';
            setTimeout(() => {
                btn.innerHTML = '<i class="fa-solid fa-clone mr-1"></i> Copiar Mensagem';
            }, 2500);
        }
    });
}

/**
 * Efeito translúcido dinâmico com mouse tracking (Spotlight / Glass Glow)
 */
function inicializarEfeitoTranslúcidoMouse() {
    document.querySelectorAll('.glass-card').forEach(card => {
        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;

            card.style.setProperty('--mouse-x', `${x}px`);
            card.style.setProperty('--mouse-y', `${y}px`);
        });
    });
}

document.addEventListener("DOMContentLoaded", () => {
    if (document.getElementById('listaApiStatus')) {
        carregarStatusAPIs();
        setInterval(carregarStatusAPIs, 60000);
    }
    inicializarEfeitoTranslúcidoMouse();
});
