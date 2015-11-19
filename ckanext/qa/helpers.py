from ckan.plugins import toolkit as tk


def qa_openness_stars_resource_html(resource):
    qa = resource.get('qa')
    if not qa:
        return '<!-- No qa info for this resource -->'
    extra_vars = qa
    return tk.literal(
        tk.render('qa/openness_stars.html',
                  extra_vars=extra_vars))


def qa_openness_stars_dataset_html(dataset):
    qa = dataset.get('qa')
    if not qa:
        return '<!-- No qa info for this dataset -->'
    extra_vars = qa
    return tk.literal(
        tk.render('qa/openness_stars_brief.html',
                  extra_vars=extra_vars))
