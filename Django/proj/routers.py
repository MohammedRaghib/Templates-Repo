class ProjectRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'erp':
            return 'erp'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'erp':
            return None
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'erp':
            return db == 'erp'
        
        if db == 'erp':
            return False
            
        return 'default'