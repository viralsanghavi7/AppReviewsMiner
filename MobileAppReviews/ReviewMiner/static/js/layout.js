/**
 * Created by Viral on 11/10/2014.
 */

var $ = window.$;

var divIdChange = "";
     function changeSelection(divId){



                $(divIdChange).removeClass("criteria_links_click");
                divIdChange = "#criteria_" + divId + "";

                document.getElementById('Performance').style.display = 'none';
                document.getElementById('UserInterface').style.display = 'none';
                document.getElementById('Compatibility').style.display = 'none';
                document.getElementById('Request').style.display = 'none';
                document.getElementById('General').style.display = 'none';
                document.getElementById('all_reviews').style.display = 'none';
                document.getElementById(divId).style.display = 'block';

                $('#criteria_links').height(
                    $(divId).height()
                );

                $(divIdChange).addClass("criteria_links_click");



            }

    function displayAll(){

    //            document.getElementById('Performance').style.display = 'block';
    //            document.getElementById('UserInterface').style.display = 'block';
    //            document.getElementById('Compatibility').style.display = 'block';
    //            document.getElementById('Request').style.display = 'block';
    //            document.getElementById('General').style.display = 'block';
    //            changeCriteriaDivHeight();

    }

    function changeCriteriaDivHeight(){
    //            $('#criteria_links').height(
    //                $('#Performance').height() + $('#UserInterface').height() + $('#Compatibility').height() + $('#Request').height() +
    //                   $('#General').height() + 300
    //
    //            );
    }

    $( document ).ready(function() {
        changeSelection("all_reviews");

    });

