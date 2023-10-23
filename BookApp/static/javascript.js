function HideShowDiv(val)
{
    if (val==1)
    {
    document.getElementById('div').style.display='none';
    var inputElement = document.getElementById('Est_in');
    inputElement.required = false;
    }

        if (val==2)
    {
    document.getElementById('div').style.display='block';
    var inputElement = document.getElementById('Est_in');
    inputElement.required = true;
    }
}
