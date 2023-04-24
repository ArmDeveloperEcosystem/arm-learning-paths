var digitalData={};


(() => {
      // Always check local storage to keep these attributes constant:
        // Theme  (light, dark)
        // Width  (is-full-width)
        // Height (expanded-masthead and contextual data)
    	//Check Storage. Keep user preference on page reload



	if (localStorage.getItem('theme')=='dark') {
    document.querySelector('html').setAttribute('theme', 'dark');
    //document.getElementById('prism-code-theme').href='/css/prism-dark.css';
	}
	else if (localStorage.getItem('theme')=='light') {
    document.querySelector('html').setAttribute('theme', 'light');
    //document.getElementById('prism-code-theme').href='/css/prism-light.css';
  }



    if (localStorage.getItem('smallerWidth')) {
        document.getElementById("all-content-div").classList.remove("is-full-width");
        document.getElementById("all-content-div-margined").classList.remove("u-margin-left-2");
        document.getElementById("all-content-div-margined").classList.remove("u-margin-right-2");
	} 
  if (localStorage.getItem('fullHeight')) {
    document.getElementById('global-nav-example-default').contextualData = []; // Hide seoncary nav on Global Nav   
    document.getElementById('global-nav-example-default').contextualIcons = []; // Hide seoncary nav on Global Nav         
    document.getElementById("expanded-masthead").setAttribute('hidden',true);  // Hide title
    document.getElementById("arm-footer").setAttribute('hidden',true);      // Hide footer
    document.getElementById("only-breadcrumb-masthead").removeAttribute('hidden'); // Show just breadcrumbs
  } 


  })();




