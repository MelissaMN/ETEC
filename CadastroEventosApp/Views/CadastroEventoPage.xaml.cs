using CadastroEventosApp.Models;

namespace CadastroEventosApp.Views;

public partial class CadastroEventoPage : ContentPage
{
    private Evento _evento;

    public CadastroEventoPage()
    {
        InitializeComponent();

        _evento = new Evento();
        BindingContext = _evento;

        dpDataTermino.MinimumDate = _evento.DataInicio;
    }

    private void OnDataInicioSelected(object sender, DateChangedEventArgs e)
    {
        if (e.NewDate is not DateTime novaData)
        {
            return;
        }

        dpDataTermino.MinimumDate = novaData;
        if (_evento.DataTermino < novaData)
        {
            _evento.DataTermino = novaData;
        }
    }

    private async void OnCadastrarClicked(object sender, EventArgs e)
    {
        if (string.IsNullOrWhiteSpace(_evento.Nome) || string.IsNullOrWhiteSpace(_evento.Local))
        {
            await DisplayAlert("Atenção", "Por favor, preencha o nome e o local do evento.", "OK");
            return;
        }

        if (_evento.NumeroParticipantes <= 0)
        {
            await DisplayAlert("Atenção", "O número de participantes deve ser maior que zero.", "OK");
            return;
        }

        await Navigation.PushAsync(new ResumoEventoPage(_evento));
    }
}