jQuery(document).ready(function() {

	  jQuery('.second-menu .dropdown').click(function() {
		  jQuery('#menu-contributors').toggle();
		  jQuery('#menu-contributors-french0').toggle();
		  jQuery('#menu-contributors-indonesian0').toggle();
	  });

	  jQuery('.nav-second .search').click(function() {
		  jQuery('#header-searchbox').toggle();
	  });
	  jQuery('.navbar-header .search').click(function() {
		  jQuery('#header-searchbox').toggle();
		  jQuery('#header-searchbox').addClass('mobile');
	  });
	  
	  jQuery(document).mouseup(function (e)
	  {
		  var container = jQuery("#header-searchbox");
	  
		  if (!container.is(e.target) // if the target of the click isn't the container...
			  && container.has(e.target).length === 0) // ... nor a descendant of the container
		  {
			  container.hide();
		  }
	  });
	  
	  jQuery('.lang_sel_sel').append( " <span class='caret'></span>" );
	  jQuery('html').click(function(e) {
	   if(jQuery(e.target).parents().index(jQuery('#menu-contributors')) == -1 ) {
			if(!jQuery(e.target).hasClass('button') && !jQuery(e.target).hasClass('dropdown') && jQuery('#menu-contributors').css('display') == 'block')
		   {
		   jQuery("#menu-contributors").hide();
		   }
		 }
	  });	
	  
	  if (window.location.href.indexOf("developer-docs") >= 0) {
		  jQuery("body").addClass("developer");
		  jQuery("span.dropdown").show();
		  jQuery("#menu-coders").show();
		  jQuery("li.menu-for-contributors").addClass("active");
	  }
	  
	  
	  else if (window.location.href.indexOf("user-docs") >= 0) {
    	  jQuery("body").addClass("user");
		  jQuery("#menu-for-users").show();
		  jQuery(".menu-for-users").addClass("active");
      }
	  else {
		  jQuery("body").addClass("orange");
		  jQuery("#menu-about").show();
		  jQuery(".menu-about").addClass("active");
	  }

});	
