

        $(document).ready(function(){
            $.getJSON("http:/static/courses/data/file.json", function(data){
                $.each(data,function(){
                    $('#history-course').append( "<div class='property-card'>"+"<div class='property-image'>"+"<div class='property-image-title'>"+"</div>"+"</div>"+"<div class='property-description'>"+"<h5>"+ this.massgtitle+"</h5>"+"<p>"+this.about+"</p>"+"<p>"+this.from+"</p>"+"</div>"+"</div>");
                    
                });
            });
        });

    $( document ).ready(function() {

        $( ".cross" ).hide();
        $( ".menu" ).hide();
        $( ".hamburger" ).click(function() {
        $( ".menu" ).slideToggle( "slow", function() {
        $( ".hamburger" ).hide();
        $( ".cross" ).show();
        });
        });
        
        $( ".cross" ).click(function() {
        $( ".menu" ).slideToggle( "slow", function() {
        $( ".cross" ).hide();
        $( ".hamburger" ).show();
        });
        });
        });




        
        var massege = document.getElementById("history-course");
        massege=document.getElementsByClassName("property-card")
        massege.onclick=function(){
            hide(massege)
            
        }
        function hide(elementhide) {
                elementhide.style.display = "none";
            
        }       
     

   
       