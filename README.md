# Trabalho de Compiladores ✅
O compilador está sendo implementado como trabalho final da disciplina de compiladores no curso Engenharia de Computação no IFMG - Campus Bambuí.
Os alunos responsáveis pelo compilador são:
- Herik Aparecida Ramos da Silva
- Jorge Luis Vieira Murilo
- Lucas Batista dos Santos

# Informação da Linguagem :information_source:
descrição...

# Lista de Tarefas 📝
- [x] Analisador Léxico
- [ ] Analisador Semântico
- [ ] Analisador Sintático

<!-- DOCUMENTAÇÃO DA LINGUAGEM CONSTRUIDA EM HTML -->
<style>
    .comment {
        color: #00ffff;
    }
    .reserved {
        color: #00b4ff;
    }
    .type {
        color: #ffc600;
    }
    code {
        color: #FFF;
    }
</style>
<h1>Sumário</h1>
<ol>
    <li><a href="#introducao">Introdução</a></li>
</ol>
<div>
    <section id="introducao">
        <h2>Introdução</h2>
        Nos exemplos a seguir, será apresentado alguns trechos de código da línguagem para exemplificar a sua utilização.
        <h2>Somando números</h2>
        <code>
            <p class="comment">/%/ Isso é um comentário.</p>
            <span class="reserved">PRINCIPAL</span> # <span class="comment">/%/ Escopo Principal</span><br>
                &nbsp;&nbsp;&nbsp;&nbsp;<span class= "type">INTEIRO</span> resultado; <br>
                &nbsp;&nbsp;&nbsp;&nbsp;<span class= "type">INTEIRO</span> x <span class="reserved"><=</span> 2; <br>
                &nbsp;&nbsp;&nbsp;&nbsp;<span class= "type">INTEIRO</span> y <span class="reserved"><=</span> 5; <br>
                <br>
                &nbsp;&nbsp;&nbsp;&nbsp;<span class="comment">/%/ Atribuindo o resultado da soma de x e y (resultado 7) </span><br>
                &nbsp;&nbsp;&nbsp;&nbsp;resultado <span class="reserved"><=</span> x <span class="reserved">+</span> y; <br>
            #  
        </code>
    </section>
</div>