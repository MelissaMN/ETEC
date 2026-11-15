# Cadastro de Eventos (.NET MAUI)

Projeto desenvolvido em .NET MAUI para cadastro e resumo de eventos utilizando `BindingContext`, `DateTime` e `TimeSpan`.

## Como rodar no VS Code

1. Certifique-se de ter o **.NET SDK** (com a workload `maui` instalada: `dotnet workload install maui`) e a extensão oficial **.NET MAUI** instalada no VS Code.
2. Abra a pasta `CadastroEventosApp` no VS Code (`File > Open Folder...`).
3. Abra o terminal integrado (`Ctrl + '`) e restaure os pacotes:
   ```bash
   dotnet restore
   ```
4. Pressione `Ctrl + Shift + P`, digite **`.NET: Select Startup Project`** e escolha `CadastroEventosApp`.
5. Selecione o alvo (Windows, Android Emulator, iOS Simulator ou MacCatalyst) na barra inferior do VS Code (ícone `{}`) ou rode via terminal:
   - **Windows:** `dotnet build -t:Run -f net8.0-windows10.0.19041.0`
   - **Android:** `dotnet build -t:Run -f net8.0-android`
   - **MacCatalyst:** `dotnet build -t:Run -f net8.0-maccatalyst`
