def statistical_outilier_removal(kdtree, k=8, z_max=2 ):
  """ Compute a Statistical Outlier Removal filter on the given KDTree.

  Parameters
  ----------                        
  kdtree: scipy's KDTree instance
      The KDTree's structure which will be used to
      compute the filter.

  k(Optional): int
      The number of nearest neighbors wich will be used to estimate the 
      mean distance from each point to his nearest neighbors.
      Default : 8

  z_max(Optional): int
      The maximum Z score wich determines if the point is an outlier or 
      not.

  Returns
  -------
  sor_filter : boolean array
      The boolean mask indicating wherever a point should be keeped or not.
      The size of the boolean mask will be the same as the number of points
      in the KDTree.

  Notes
  -----    
  The 2 optional parameters (k and z_max) should be used in order to adjust
  the filter to the desired result.

  A HIGHER 'k' value will result(normally) in a HIGHER number of points trimmed.

  A LOWER 'z_max' value will result(normally) in a HIGHER number of points trimmed.

  """

  distances, i = kdtree.query(kdtree.data, k=k, n_jobs=-1) 

  z_distances = stats.zscore(np.mean(distances, axis=1))

  sor_filter = abs(z_distances) < z_max

  return sor_filter
