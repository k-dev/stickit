var XMLHttpFactories = [
        function ( )
          {
          return ( new XMLHttpRequest ( ) );
          },
        function ( )
          {
          return ( new ActiveXObject ( "Msxml2.XMLHTTP" ) );
          },
        function ( )
          {
          return ( new ActiveXObject ( "Msxml3.XMLHTTP" ) );
          },
        function ( )
          {
          return ( new ActiveXObject ( "Microsoft.XMLHTTP" ) );
          }
        ];

// ********************************************** createXMLHTTPObject

function createXMLHTTPObject()
{
    var xmlhttp = false;

    for ( var i = 0; ( i < XMLHttpFactories.length ); i++ )
      {
      try
        {
        xmlhttp = XMLHttpFactories [ i ] ( );
        }

      catch ( e )
        {
        continue;
        }

      break;
      }

    return ( xmlhttp );
}

// **************************************************** read_contents

function read_contents ( url )
{
    var request = createXMLHTTPObject ( );

    request.open ( 'GET', url, false );
    request.setRequestHeader ( 'Content-Type', 'text/html' );
    request.send ( '' );

    return ( request.responseText );
}

function place_in_outerHTML ( element, 
                            contents )
{

    if ( element.outerHTML )
      {
      element.outerHTML = contents;
      }
    else
      {
      element.innerHTML = contents;    
      }
}

function add_header ( page_name, content_path )
{
      {
      var header = document.getElementById ( 'header' );

      if ( header )
        {
         // var header_contents = read_contents ( "header/header_content.txt" );
         var header_contents = read_contents ( content_path );
      
        if ( header_contents )
          {
/*
          header_contents = header_contents.replace ( 
                                              '{{SiteLogoTarget}}',
                                              site_logo_target );
          header_contents = header_contents.replace ( 
                                              '{{SiteLogo}}',
                                              site_logo );
          header_contents = header_contents.replace ( 
                                              '{{PageHeader}}',
                                              page_header );
          header_contents = header_contents.replace ( 
                                              '{{PageSubHeader}}',
                                              page_subheader );
*/
                                              
          place_in_outerHTML ( header, header_contents );
          }
        }
      }  

}