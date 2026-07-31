(function (global) {
  "use strict";

  global.FEK_FLOW_WORKFLOW_TEMPLATE = [
    {
      "name": "1. Solicitação de Desenvolvimento",
      "disciplines": [
        {
          "name": "Entradas e requisitos",
          "tasks": [
            "Identificar solicitante e área",
            "Definir cliente, aplicação e família do produto",
            "Registrar capacidade de carga e dimensões",
            "Registrar configurações e opcionais",
            "Anexar referências e documentos",
            "Indicar requisitos legais",
            "Definir prazo solicitado",
            "Verificar suficiência das entradas",
            "Aprovar ou devolver a SD"
          ]
        }
      ]
    },
    {
      "name": "2. Análise Crítica",
      "disciplines": [
        {
          "name": "Viabilidade e planejamento",
          "tasks": [
            "Analisar viabilidade técnica",
            "Verificar normas e resoluções",
            "Avaliar projetos semelhantes",
            "Definir projeto novo ou derivação",
            "Identificar setores impactados",
            "Avaliar recursos e capacidade",
            "Registrar riscos iniciais",
            "Definir cronograma e responsáveis",
            "Avaliar ferramental e impacto produtivo",
            "Emitir parecer da análise crítica"
          ]
        }
      ]
    },
    {
      "name": "3. Detalhamento Multidisciplinar",
      "disciplines": [
        {
          "name": "Estrutura",
          "tasks": [
            "Determinar capacidade de carga",
            "Definir geometria geral",
            "Calcular distribuição de carga",
            "Determinar reações no pino-rei e suspensão",
            "Verificar PBT e PBTC",
            "Definir eixos e suspensão",
            "Selecionar matéria-prima",
            "Verificar limites dimensionais",
            "Analisar interferências",
            "Gerar modelo 3D e desenhos",
            "Executar FEA quando aplicável"
          ]
        },
        {
          "name": "Caixa e acabamento",
          "tasks": [
            "Dimensionar caixa de carga",
            "Definir capacidade volumétrica",
            "Selecionar matéria-prima",
            "Definir sinalização e faixas refletivas",
            "Gerar modelos e desenhos"
          ]
        },
        {
          "name": "Montagem",
          "tasks": [
            "Realizar montagem geral 3D",
            "Simular movimentos",
            "Analisar montabilidade",
            "Verificar acesso de ferramentas",
            "Gerar instrução de montagem",
            "Gerar prospecto e desenho para AET"
          ]
        },
        {
          "name": "Sistemas",
          "tasks": [
            "Definir suspensão",
            "Dimensionar suportes e vigas de eixo",
            "Definir sistema hidráulico",
            "Definir sistema pneumático",
            "Definir sistema elétrico",
            "Gerar diagramas e listas técnicas"
          ]
        }
      ]
    },
    {
      "name": "4. Revisão, Aprovação e Liberação",
      "disciplines": [
        {
          "name": "Documentação Técnica",
          "tasks": [
            "Conferir identificação e revisão",
            "Conferir vistas, cotas e tolerâncias",
            "Conferir matéria-prima",
            "Verificar lista de materiais",
            "Verificar peças duplicadas",
            "Controlar arquivos obsoletos",
            "Aprovar ou devolver desenhos",
            "Cadastrar códigos e liberar BOM"
          ]
        }
      ]
    },
    {
      "name": "5. Produção e Protótipo",
      "disciplines": [
        {
          "name": "Produção",
          "tasks": [
            "Solicitar Ordem de Produção",
            "Apresentar projeto à fábrica",
            "Acompanhar fabricação das peças",
            "Acompanhar montagem final",
            "Registrar dificuldades e alterações",
            "Verificar dimensões",
            "Realizar pesagem",
            "Comparar tara real e prevista"
          ]
        }
      ]
    },
    {
      "name": "6. Verificação e Validação",
      "disciplines": [
        {
          "name": "Validação multidisciplinar",
          "tasks": [
            "Colher parecer da Engenharia",
            "Colher parecer da Produção",
            "Colher parecer de Processos",
            "Colher parecer da Qualidade",
            "Colher parecer de PCP, Compras e Custos",
            "Avaliar montabilidade e conformidade",
            "Anexar FEA e FMEA",
            "Executar teste de campo",
            "Registrar aceite do cliente",
            "Aprovar, corrigir ou reprovar protótipo"
          ]
        }
      ]
    },
    {
      "name": "7. Homologação e Configurador",
      "disciplines": [
        {
          "name": "Homologação",
          "tasks": [
            "Preparar memorial e desenhos",
            "Reunir relatórios de ensaio",
            "Confirmar CCT",
            "Protocolar CAT",
            "Responder exigências",
            "Obter código Marca/Modelo/Versão"
          ]
        },
        {
          "name": "Configurador",
          "tasks": [
            "Conferir BOM 150%",
            "Cadastrar variáveis e opcionais",
            "Informar TARA e RENAVAM",
            "Testar combinações",
            "Aprovar configurador",
            "Emitir lançamento"
          ]
        }
      ]
    },
    {
      "name": "8. Pós-lançamento e Alterações",
      "disciplines": [
        {
          "name": "Alterações",
          "tasks": [
            "Abrir SA",
            "Analisar impacto em estoque, ferramental e custos",
            "Atualizar desenhos e BOM",
            "Comunicar áreas impactadas",
            "Atualizar catálogos e manuais",
            "Bloquear produtos inativos"
          ]
        },
        {
          "name": "Conhecimento",
          "tasks": [
            "Registrar falhas de campo",
            "Registrar lições aprendidas",
            "Vincular decisão técnica ao componente",
            "Atualizar banco de conhecimento"
          ]
        }
      ]
    }
  ];
})(window);
