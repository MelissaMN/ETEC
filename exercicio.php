<?php

$produtos = [
    "Arroz" => 20,
    "Feijão" => 45,
    "Macarrão" => 70,
    "Café" => 15,
    "Açúcar" => 55
];

function verificarEstoqueBaixo($quantidade)
{
    return $quantidade < 50;
}

function mostrarEstoque($produtos)
{
    foreach ($produtos as $produto => $quantidade) {
        echo "Produto: $produto - Quantidade: $quantidade<br>";

        if (verificarEstoqueBaixo($quantidade)) {
            echo "Estoque baixo!<br>";
        }

        echo "<br>";
    }
}

mostrarEstoque($produtos);

?>