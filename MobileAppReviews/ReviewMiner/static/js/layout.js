/**
 * Created by Viral on 11/10/2014.
 */

 function changeSelection(divId){

            document.getElementById('Performance').style.display = 'none';
            document.getElementById('UserInterface').style.display = 'none';
            document.getElementById('Compatibility').style.display = 'none';
            document.getElementById('Request').style.display = 'none';
            document.getElementById('General').style.display = 'none';
            document.getElementById(divId).style.display = 'block';

        }

        function displayAll(){

            document.getElementById('Performance').style.display = 'block';
            document.getElementById('UserInterface').style.display = 'block';
            document.getElementById('Compatibility').style.display = 'block';
            document.getElementById('Request').style.display = 'block';
            document.getElementById('General').style.display = 'block';
        }
