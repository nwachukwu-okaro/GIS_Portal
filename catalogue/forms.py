from django import forms

TYPE_CHOICES = [
    ('Map', 'Map'),
    ('Dataset', 'Dataset'),
    ('Report', 'Report'),
    ('Service', 'Service'),
]

ACCESS_CHOICES = [
    ('Internal', 'Internal'),
    ('Restricted', 'Restricted'),
    ('Public', 'Public'),
]

SPATIAL_FILE_EXTENSIONS = {'.gpkg', '.csv', '.geojson', '.json'}


class MetadataForm(forms.Form):
    """The 10 required metadata fields shared by every upload form."""

    title = forms.CharField(max_length=200)
    abstract = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))
    keywords = forms.CharField(
        help_text='Separate multiple keywords with commas, e.g. roads, transport, survey.'
    )
    aoi = forms.CharField(
        label='Area of Interest',
        help_text=(
            'A known area name (medway, kent, london, uk) or a bounding box '
            'as xmin,ymin,xmax,ymax.'
        ),
    )
    type = forms.ChoiceField(choices=TYPE_CHOICES)
    organisation = forms.CharField(max_length=200)
    team = forms.CharField(max_length=200)
    access = forms.ChoiceField(label='Access level', choices=ACCESS_CHOICES)
    project = forms.CharField(max_length=200)
    contact = forms.EmailField(label='Contact email')


class UploadForm(MetadataForm):
    bucket = forms.ChoiceField()
    file = forms.FileField()

    def __init__(self, *args, buckets=(), **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['bucket'].choices = [(b, b) for b in buckets]


class SpatialUploadForm(MetadataForm):
    schema = forms.ChoiceField(label='Schema')
    file = forms.FileField(
        help_text='GeoPackage (.gpkg), CSV (.csv), or GeoJSON (.geojson/.json).'
    )

    def __init__(self, *args, schemas=(), **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['schema'].choices = [(s, s) for s in schemas]

    def clean_file(self):
        uploaded_file = self.cleaned_data['file']
        parts = uploaded_file.name.rsplit('.', 1)
        ext = f'.{parts[1].lower()}' if len(parts) == 2 else ''
        if ext not in SPATIAL_FILE_EXTENSIONS:
            raise forms.ValidationError(
                'Please upload a GeoPackage (.gpkg), CSV (.csv), or GeoJSON (.geojson) file.'
            )
        return uploaded_file
