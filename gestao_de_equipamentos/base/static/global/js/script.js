const body = document.querySelector("body"),
      sidebar = body.querySelector(".sidebar"),
      toggle = body.querySelector(".toggleSidebar"),
      modeSwitch = body.querySelector(".toggle-switch"),
      modeText = body.querySelector(".mode-text");
      


    function toggledarkmode(){
      body.classList.toggle("dark");
    }

    function loadtheme() {
      const darkmode = localStorage.getItem("dark")

      if(darkmode) {
        toggledarkmode();
      }
      if(darkmode){
        modeText.innerText = "Modo Claro"
      }
    }

    loadtheme();

      modeSwitch.addEventListener("click", () =>{
        toggledarkmode();

        localStorage.removeItem("dark");

        if(body.classList.contains("dark")){
          localStorage.setItem("dark", 1)
        }
        if(body.classList.contains("dark")){
          modeText.innerText = "Modo Claro"
        }else{
          modeText.innerText = "Modo Escuro"
        }

      });
      
      function togglesidenav(){
        sidebar.classList.toggle("closer");
      }
  
      function loadsidebar() {
        const sidebarclose = localStorage.getItem("closer")
  
        if(sidebarclose) {
          togglesidenav();
        }
        
      }
  
      loadsidebar();

      toggle.addEventListener("click", () =>{
        togglesidenav();
  
        localStorage.removeItem("closer");

        if(sidebar.classList.contains("closer")){
          localStorage.setItem("closer", 2)
        }
      });




      $( document ).ready(function() {
        var baseUrl    = window.location.origin + '/equipamentos/';
        var urlatual   = window.location.href;
        var searchBtn  = $('#search-btn');
        var Tags       = $('#tags_filtro');
        var searchForm = $('#search-form');
        var Search     = $('#search');
        var Filter     = $('#filter');
        var clear      = $('#clear-search');
        var detalhe    = $('#id_detalhar');
        var detalhes_equipamentos = $('#detalhes_equipamentos');
        var Marcar_todos_lido = $('#marcar_lido');


      let tag = $('#search-form').data('tags_filtro');
      if (tag) {
        $('#tags_filtro option[value='+tag+']').attr('selected', 'selected');
      };

      

      let Marcar_lido_visualizar = window.location.pathname.split('/')[2];
      let Marcar_lido_laboratorio_ou_tag = window.location.pathname.split('/')[1];
      
      if (Marcar_lido_visualizar == 'visualizar' || Marcar_lido_laboratorio_ou_tag == 'laboratorios' || Marcar_lido_laboratorio_ou_tag == 'tags') {
        $('#marcar_lido').submit();
      };

      $(searchBtn).on('click', function() {
        searchForm.submit();
      });
      $(clear).on('click', function() {
        Search.val('');
        $('#search-btn').click();
      });
      $(Tags).change(function() {
        $('#search-btn').click();
      });
      $(Filter).change(function() {
        var Filter = $(this).val();
        localStorage.setItem(3, Filter);
        if (Search.val()) {
          $('#clear-search').click();
        } else {
          $('#search-btn').click();
        };
      });
      var filtro = localStorage.getItem(3);
      if (filtro) {
        var filtrar = $('#filter option[value='+filtro+']').attr('selected', 'selected');
        if (baseUrl==urlatual) {
          if (filtrar.length == 0) {
            var filtrar = $('#filter option').eq(0).attr('selected', 'selected');
            var filtrar = filtrar.val();
            localStorage.setItem(3, filtrar);
          };
        };
      };
      if (baseUrl==urlatual) {
        var filtro = localStorage.getItem(3);
        if (filtro) {
          $('#search-btn').click();
        };
      };
      var detalhar = ($(detalhe).is(":checked"));
      if (detalhar == true) {
        $(detalhes_equipamentos).removeClass("hidden");
      } else {
        $(detalhes_equipamentos).addClass("hidden");
      };
      $(detalhe).on('click', function() {
        var detalhe = $(this).is(":checked");
        console.log(detalhe)
        if (detalhe == true) {
          $(detalhes_equipamentos).removeClass("hidden");
        } else {
          $(detalhes_equipamentos).addClass("hidden");
        };
    });
   });



function destacarPaginaAtualSidebar() {
  let url = window.location.pathname;
  let nomePaginaAtual = url.split('/')[1];
  let opcaoSidebar = document.getElementById(nomePaginaAtual);
  if (opcaoSidebar) {
    opcaoSidebar.classList.add('pagina-atual');
  }
}
  

function atualizarDimensoesRodape() {
  let rodape = document.getElementById('rodape');
  let altura = rodape.getBoundingClientRect().height;
  rodape.style.bottom = -altura + 'px';
}

window.addEventListener('resize', atualizarDimensoesRodape);

destacarPaginaAtualSidebar();
atualizarDimensoesRodape();