from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['snacks'] = [
            {
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/6/69/Potato-Chips.jpg",
                "title": "Potato Chip",
                "description": "Also known as a crisp",
                "reference_url": "https://en.wikipedia.org/wiki/Potato_chip"
            }, {
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/8/83/French_Fries.JPG",
                "title": "Potato Chips",
                "description": "Also known as french fries",
                "reference_url": "https://en.wikipedia.org/wiki/French_fries"
            }, {
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/8/89/NXP_PCF8577C_LCD_driver_with_I%C2%B2C_%28Colour_Corrected%29.jpg",
                "title": "Micro Chip",
                "description": "Not edible",
                "reference_url": "https://en.wikipedia.org/w/index.php?title=Micro_chip"
            },
        ]

        return context


class AboutView(TemplateView):
    template_name = 'about.html'