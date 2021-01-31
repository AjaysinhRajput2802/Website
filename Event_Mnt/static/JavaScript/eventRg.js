function validate() {
    start=document.getElementById("periodSt").value;
    end=document.getElementById("periodEnd").value;
    if (start>end)
    {
        document.getElementById("alert").style.visibility="visible";
    }
}