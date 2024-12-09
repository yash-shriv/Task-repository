import psutil
from django.shortcuts import render

# Create your views here.
def home(request):
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent', 'create_time', 'username']):
        try:
            processes.append({
                'pid': proc.info['pid'],
                'name': proc.info['name'],
                'cpu_percent': proc.info['cpu_percent'],
                'memory_percent': proc.info['memory_percent'],
                'create_time': proc.info['create_time'],
                'username': proc.info['username'],
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    query = request.GET.get('q', '')
    if query:
        processes = [p for p in processes if query.lower() in str(p['pid']).lower() or query.lower() in p['name'].lower()]

    sort_by = request.GET.get('sort', '')
    if sort_by:
        processes = sorted(processes, key=lambda x: x.get(sort_by, ''))

    context = {'processes': processes, 'query': query, 'sort_by': sort_by}
    return render(request, 'spma_app/home.html', context)
