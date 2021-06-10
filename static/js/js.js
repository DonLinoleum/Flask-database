/* Кнопки слева */
let SnrButtonLeft = document.getElementById("SnrButton");
let StbButtonLeft = document.getElementById("StbButton");
/*  Главный список  */
let SNR_div = document.getElementById("SNR");
let STB_div = document.getElementById("STB");
let SNR_arenda_div = document.getElementById ("SNR_ARENDA");
let STB_arenda_div = document.getElementById ("STB_ARENDA");
/* Кнопки справа  */
let AddButton = document.getElementById("AddButton");
let DelButton = document.getElementById("DelButton");
let AddArendaButton = document.getElementById ("ArendaButton");
let RemoveArendaButton = document.getElementById ("DelArendaButton");
/* Div с ошибкой  */
let DivWarning = document.getElementById ("warning");

SnrButton.style.backgroundColor = "rgb(76, 73, 84)";

/* Кнопки слева  */
SnrButtonLeft.addEventListener('click',function(e){
	STB_div.style.display="none";
	STB_arenda_div.style.display = "none";
	SNR_arenda_div.style.display = "block";
	SNR_div.style.display="block";
	SnrButtonLeft.style.backgroundColor = "rgb(76, 73, 84)";
	StbButtonLeft.style.backgroundColor = "inherit";
})

StbButtonLeft.addEventListener ('click',function(e){
	STB_div.style.display="block";
	STB_arenda_div.style.display = "block";
	SNR_arenda_div.style.display = "none";
	SNR_div.style.display="none";
	StbButtonLeft.style.backgroundColor = "rgb(76, 73, 84)";
	SnrButtonLeft.style.backgroundColor = "inherit";
});

/* Обработка добавления */
AddButton.addEventListener('click',function(e){

	if (SnrButtonLeft.style.backgroundColor == "rgb(76, 73, 84)")
	{document.location.href="/addsnr";}
	if (StbButtonLeft.style.backgroundColor == "rgb(76, 73, 84)")
	{document.location.href="/addstb"} 
});
/* Обработка удаления */
DelButton.addEventListener('click',function(){
	let radios_snr = document.getElementsByName('snr');
	let radios_stb = document.getElementsByName('stb');
	
	let NumOfSnrChecked = 0;
	let NumsOfStbChecked = 0;
	
	for (var i = 0; i<radios_snr.length;i++)
	{
		if (radios_snr[i].checked)
		{			
			document.location.href="/delsnr/"+ radios_snr[i].value;
		}
		else
		{
			NumOfSnrChecked++;
		}
	}
	for (var i = 0; i<radios_stb.length;i++)
	{
		if (radios_stb[i].checked)
		{		
			document.location.href="/delstb/"+ radios_stb[i].value;
		}
		else
		{
			NumsOfStbChecked++;
		}
	}
	if (NumOfSnrChecked ===radios_snr.length && NumsOfStbChecked===radios_stb.length)
	{
		DivWarning.style.display = "block";
		DivWarning.style.opacity = "1";
		DivWarning.innerText = "Ошибка, не выбран элемент в наличии для удаления!";		
	}
})
/* Обработка добавления в аренду */
AddArendaButton.addEventListener('click',function(e){
	
	let radios_snr = document.getElementsByName('snr');
	let radios_stb = document.getElementsByName('stb');
	
	let NumOfSnrChecked = 0;
	let NumOfStbChecked = 0;
			
	if (SnrButtonLeft.style.backgroundColor == "rgb(76, 73, 84)")
	{
		for (var i = 0; i<radios_snr.length;i++)
	{
		if (radios_snr[i].checked)
		{			
			document.location.href="addsnrarenda/"+ radios_snr[i].value;
		}
		else 
		{
			NumOfSnrChecked++;
		}
	}
	if (NumOfSnrChecked ===radios_snr.length)
		{
			DivWarning.style.display = "block";
			DivWarning.style.opacity = "1";
			DivWarning.innerText = "Ошибка, не выбран SNR в наличии для передачи в аренду!";					
		}
		
	}
	
	if (StbButtonLeft.style.backgroundColor == "rgb(76, 73, 84)")
	{
		for (var i = 0; i<radios_stb.length;i++)
		{
			if (radios_stb[i].checked)
			{		
				document.location.href="addstbarenda/"+ radios_stb[i].value;
			}
			else 
			{
				NumOfStbChecked++;
			}
		}
		if (NumOfStbChecked ===radios_stb.length)
		{
			DivWarning.style.display = "block";
			DivWarning.style.opacity = "1";
			DivWarning.innerText = "Ошибка, не выбран STB в наличии для передачи в аренду!";					
		}		
	}	
});
/* Обработка удаления из аренды */
RemoveArendaButton.addEventListener('click',function(e){
	
	let radios_snr = document.getElementsByName('snr_arenda');
	let radios_stb = document.getElementsByName('stb_arenda');
	
	let NumOfSnrChecked = 0;
	let NumOfStbChecked = 0;
			
	if (SnrButtonLeft.style.backgroundColor == "rgb(76, 73, 84)")
	{
		for (var i = 0; i<radios_snr.length;i++)
	{
		if (radios_snr[i].checked)
		{			
			document.location.href="delsnrarenda/"+ radios_snr[i].value;
		}
		else 
		{
			NumOfSnrChecked++;
		}
	}
	if (NumOfSnrChecked ===radios_snr.length)
		{
			DivWarning.style.display = "block";
			DivWarning.style.opacity = "1";
			DivWarning.innerText = "Ошибка, не выбран SNR в аренде!";					
		}
		
	}
	
	if (StbButtonLeft.style.backgroundColor == "rgb(76, 73, 84)")
	{
		for (var i = 0; i<radios_stb.length;i++)
		{
			if (radios_stb[i].checked)
			{		
				document.location.href="delstbarenda/"+ radios_stb[i].value;
			}
			else 
			{
				NumOfStbChecked++;
			}
		}
		if (NumOfStbChecked ===radios_stb.length)
		{
			DivWarning.style.display = "block";
			DivWarning.style.opacity = "1";
			DivWarning.innerText = "Ошибка, не выбран STB в аренде!";					
		}		
	}	
});