# 🚀 Configuração do Deploy no GitHub Pages

Este documento explica como configurar o deploy automático do SQLPlay no GitHub Pages usando GitHub Actions.

## ⚠️ **Importante: Limitação do GitHub Pages**

O GitHub Pages **não suporta aplicações Django** que precisam de servidor Python. Por isso, criamos uma solução que:

1. **Gera uma versão estática** do site Django
2. **Remove todas as funcionalidades** que precisam de backend
3. **Mantém apenas a interface visual** e navegação básica

## 🔧 **Configuração Necessária**

### **1. Configurar GitHub Pages**

1. Vá para **Settings** do seu repositório
2. Role até **Pages** na barra lateral
3. Em **Source**, selecione **Deploy from a branch**
4. Em **Branch**, selecione **gh-pages** e **/(root)**
5. Clique **Save**

### **2. Configurar GitHub Actions**

O workflow `.github/workflows/deploy.yml` já está configurado e irá:

- Executar automaticamente a cada push na branch `main`
- Instalar dependências Python
- Gerar arquivos estáticos
- Fazer deploy para a branch `gh-pages`

### **3. Verificar Permissões**

1. Vá para **Settings** → **Actions** → **General**
2. Em **Workflow permissions**, selecione **Read and write permissions**
3. Marque **Allow GitHub Actions to create and approve pull requests**
4. Clique **Save**

## 📁 **Estrutura do Deploy**

### **Arquivos Gerados Automaticamente:**

```
static_site/
├── index.html              # Página inicial estática
├── jogo-da-velha.html     # Página do jogo estática
├── static/                 # CSS, JS e outros arquivos
│   ├── css/
│   ├── js/
│   └── ...
└── .nojekyll              # Desabilita processamento Jekyll
```

### **Arquivos de Configuração:**

- `.github/workflows/deploy.yml` - Workflow do GitHub Actions
- `static_build.py` - Script para gerar versão estática
- `_config.yml` - Configuração do GitHub Pages

## 🚀 **Como Funciona o Deploy**

### **Processo Automático:**

1. **Push para main** → Trigger do GitHub Actions
2. **Build** → Geração da versão estática
3. **Deploy** → Upload para branch `gh-pages`
4. **GitHub Pages** → Serve o site estático

### **Tempo de Deploy:**

- **Primeiro deploy**: 2-5 minutos
- **Deploys subsequentes**: 1-3 minutos
- **Disponibilidade**: Imediata após deploy

## 🔍 **Verificar o Deploy**

### **1. Status do Workflow:**

1. Vá para **Actions** no seu repositório
2. Clique no workflow **Deploy Django to GitHub Pages**
3. Verifique se todos os steps passaram (✅)

### **2. Branch gh-pages:**

1. Vá para **Branches**
2. Procure pela branch `gh-pages`
3. Verifique se os arquivos foram criados

### **3. Site Online:**

1. Vá para **Settings** → **Pages**
2. O link do site aparecerá em **Your site is live at**
3. Clique no link para testar

## 🐛 **Solução de Problemas**

### **Erro: "Workflow failed"**

- Verifique os logs do GitHub Actions
- Confirme se as permissões estão corretas
- Verifique se o Python 3.11 está disponível

### **Erro: "Page not found"**

- Aguarde alguns minutos após o deploy
- Verifique se a branch `gh-pages` foi criada
- Confirme se o GitHub Pages está configurado para `gh-pages`

### **Erro: "Build failed"**

- Verifique se todas as dependências estão em `requirements.txt`
- Confirme se os templates Django estão corretos
- Verifique se o script `static_build.py` está funcionando

## 📝 **Notas Importantes**

### **Limitações da Versão Estática:**

- ❌ **Sem funcionalidade do jogo** (precisa de backend)
- ❌ **Sem banco de dados** (precisa de servidor)
- ❌ **Sem autenticação** (precisa de Django)
- ✅ **Interface visual completa**
- ✅ **Navegação entre páginas**
- ✅ **Design responsivo**

### **Para Funcionalidade Completa:**

Para ter o jogo funcionando, você precisará:

1. **Deploy em servidor Python** (Heroku, PythonAnywhere, etc.)
2. **Banco de dados** (PostgreSQL, MySQL, etc.)
3. **Configuração de ambiente** (variáveis de ambiente)

## 🎯 **Próximos Passos**

1. **Configure o GitHub Pages** conforme instruções acima
2. **Faça push** para a branch `main`
3. **Monitore o deploy** na aba Actions
4. **Teste o site** no link fornecido pelo GitHub Pages
5. **Para funcionalidade completa**, considere deploy em servidor Python

## 📞 **Suporte**

Se encontrar problemas:

1. Verifique os logs do GitHub Actions
2. Confirme se todas as configurações estão corretas
3. Abra uma issue no repositório
4. Consulte a documentação do GitHub Pages

---

**Lembre-se**: Esta é uma solução temporária para mostrar a interface. Para o jogo funcionar, será necessário deploy em um servidor que suporte Django.
